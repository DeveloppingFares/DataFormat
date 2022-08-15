import os
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
        for element in elements:
            if issubclass(type(element), C_Element) or issubclass(type(element), C_Bloc):
                if not hasattr(self, element.nom):
                    setattr(self, element.nom, element)
                else:
                    raise KeyError(f"Le package {self.nom} contient deja un attribut {element.nom}")
            else:
                raise ValueError(f"L'element {element.nom} fournie pour le package {self.nom} n'est pas de type Element")

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
    def dependance(self) -> list:
        return self._dependance

    @property
    def random(self) -> bytearray:
        return bytearray(os.urandom(self.taille))

    def update(self, **kwargs) -> None:
        raise NotImplementedError

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
