import os
from Source.Data.Format import ErreurNomAttributUtilise
from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Bloc import C_Bloc
from Source.Data.Interfaces.M_Element import C_Element


class C_Package(C_observable, C_Bloc):
    def __init__(self, nom: str, description: str, dependance: list, elements: list):
        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

        # Depuis Observable
        super().__init__()

        # Depuis Bloc
        self._elements: list = elements
        if len(self._elements):
            self.ajout_elements(self._elements)

    # ==================================================================================================================
    # Depuis Donnees
    # ==================================================================================================================
    @property
    def nom(self) -> str:
        return self._nom

    @property
    def description(self) -> str:
        return self._description

    @property
    def type_element(self) -> str:
        return 'package'

    @property
    def dependance(self) -> list:
        return self._dependance

    @property
    def random(self) -> bytearray:
        return bytearray(os.urandom(self.taille))

    def ajout_elements(self, elements: list):
        self._elements = elements
        for element in self._elements:
            if issubclass(type(element), C_Element) or issubclass(type(element), C_Bloc):
                if not hasattr(self, element.nom):
                    setattr(self, element.nom, element)
                else:
                    raise ErreurNomAttributUtilise(type_element=self.__class__.__name__, nom_element=self.nom, nom_attribut=element.nom)
            else:
                raise ValueError(f"L'element {element.nom} fournie pour le package {self.nom} n'est pas de type Element")

    def ajout_dependances(self, dependances: list):
        self._dependance = dependances

    # ==================================================================================================================
    # Depuis Observer
    # ==================================================================================================================
    def ajout_observer(self):
        for dependance in self.dependance:
            dependance.ajout_observer(self)
        for attr in self.__dict__.values():
            if issubclass(type(attr), C_Element):
                attr.ajout_observer()

    def update(self, **kwargs) -> None:
        print(f"Notification de {self.nom} depuis {kwargs.get('nom_emetteur')} ({kwargs.get('type_emetteur')})")

    # ==================================================================================================================
    # Depuis Bloc
    # ==================================================================================================================
    @property
    def valeur(self) -> bytearray:
        if any(issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc) for attr in self.__dict__.values()):
            v = bytearray()
            for attr in self.__dict__.values():
                if issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc):
                    v += attr.valeur
            return v
        else:
            raise AttributeError(f"Package {self.nom} ne contient aucun élément")

    @valeur.setter
    def valeur(self, v: bytearray):
        if any(issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc) for attr in self.__dict__.values()):
            for attr in self.__dict__.values():
                if issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc):
                    attr.valeur = v[:attr.taille]
                    del v[:attr.taille]
        else:
            raise AttributeError(f"Package {self.nom} ne contient aucun élément")
        self.notify()

    @property
    def taille(self) -> int:
        t: int = 0
        if any(issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc) for attr in self.__dict__.values()):
            for attr in self.__dict__.values():
                if issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc):
                    t += attr.taille
        else:
            raise AttributeError(f"Package {self.nom} ne contient aucun élément")
        return t

    @property
    def elements(self) -> list:
        return self._elements

    def corrupt(self, type_corruption: str, element_corrompu: str, **kwargs) -> bytearray:
        corrompu = False
        if any(issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc) for attr in self.__dict__.values()):
            v = bytearray()
            for attr in self.__dict__.values():
                if issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc):
                    if attr.nom == element_corrompu:
                        v += attr._corrupt(type_corruption=type_corruption, **kwargs)
                        corrompu = True
                    else:
                        v += attr.valeur
            if not corrompu:
                raise AttributeError(f"Package {self.nom} ne contient aucun élément appele {element_corrompu}")
            return v
        else:
            raise AttributeError(f"Package {self.nom} ne contient aucun élément")