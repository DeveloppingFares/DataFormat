import os
from Source.Commun.Data.Format import ErreurNomAttributUtilise
from Source.Commun.Observer.M_observable import C_observable
from Source.Commun.Data.Interfaces.M_Donnees import C_Donnees
from Source.Commun.Data.Interfaces.M_Bloc import C_Bloc
from Source.Commun.Data.Interfaces.M_Element import C_Element
from Source.Commun.Data.Format.M_Reference import C_Reference


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
        v = bytearray()
        for attr in self.__dict__.values():
            if issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc):
                v += attr.valeur
        return v

    @valeur.setter
    def valeur(self, v: bytearray):
        for attr in self.__dict__.values():
            if issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc):
                attr.valeur = v[:attr.taille]
                del v[:attr.taille]
        self.notify()

    @property
    def taille(self) -> int:
        t: int = 0
        for attr in self.__dict__.values():
            if issubclass(type(attr), C_Element) or issubclass(type(attr), C_Bloc):
                t += attr.taille
        return t

    @property
    def elements(self) -> list:
        return self._elements

    def corrupt(self, type_corruption: str, element_corrompu: str, **kwargs) -> bytearray:
        corrompu = False
        v = bytearray()
        for attr in self.__dict__.values():
            if issubclass(type(attr), C_Element):
                if attr.nom == element_corrompu:
                    v += attr._corrupt(type_corruption=type_corruption, **kwargs)
                    corrompu = True
                # On effectue la corruption dans l'objet reference plutot que dans la référence
                elif type(attr) == C_Reference:
                    if attr.nom_variable_reference == element_corrompu:
                        v += attr._corrupt(type_corruption=type_corruption, **kwargs)
                        corrompu = True
                    elif issubclass(type(attr.reference), C_Bloc):
                        if attr.reference.has_attribut(element_corrompu):
                            v += attr.reference.corrupt(type_corruption=type_corruption, element_corrompu=element_corrompu, **kwargs)
                            corrompu = True
                    else:
                        v += attr.valeur
                else:
                    v += attr.valeur
            elif issubclass(type(attr), C_Bloc):
                if attr.nom == element_corrompu:
                    v += attr._corrupt(type_corruption=type_corruption, **kwargs)
                    corrompu = True
                elif attr.has_attribut(element_corrompu):
                    v += attr.corrupt(type_corruption=type_corruption, element_corrompu=element_corrompu, **kwargs)
                    corrompu = True
                else:
                    v += attr.valeur
        if not corrompu:
            raise AttributeError(f"Package {self.nom} ne contient aucun élément appele {element_corrompu}")
        return v

    def has_attribut(self, nom_attribut: str) -> bool:
        for attr in self.__dict__.values():
            if issubclass(type(attr), C_Bloc):
                if attr.has_attribut(nom_attribut) or attr.nom == nom_attribut:
                    return True
            elif issubclass(type(attr), C_Donnees):
                if attr.nom == nom_attribut:
                    return True
                # On effectue la recherche dans l'objet reference plutot que dans la référence
                elif type(attr) == C_Reference:
                    if attr.nom_variable_reference == nom_attribut:
                        return True
                    elif issubclass(type(attr.reference), C_Bloc):
                        if attr.reference.has_attribut(nom_attribut):
                            return True
        return False
