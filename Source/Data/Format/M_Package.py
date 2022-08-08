import os
from Source.Data.Interfaces.M_Bloc import C_Bloc
from Source.Data.Interfaces.M_Element import C_Element


class C_Package(C_Bloc):
    def __init__(self, nom: str, description: str, dependance: list, elements: list):
        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

        # Depuis Bloc
        self._elements: list = elements

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

    # ==================================================================================================================
    # Depuis Bloc
    # ==================================================================================================================
    @property
    def valeur(self) -> bytearray:
        if any(issubclass(type(attr), C_Element) for attr in self.__dict__.values()):
            v = bytearray()
            for attr in self.__dict__.values():
                if issubclass(type(attr), C_Element):
                    v += attr.valeur
            return v
        else:
            raise AttributeError(f"Package {self.nom} ne contient aucun élément")

    @valeur.setter
    def valeur(self, v: bytearray):
        if any(issubclass(type(attr), C_Element) for attr in self.__dict__.values()):
            for attr in self.__dict__.values():
                if issubclass(type(attr), C_Element):
                    attr.valeur = v[:attr.taille]
                    del v[:attr.taille]
        else:
            raise AttributeError(f"Package {self.nom} ne contient aucun élément")

    @property
    def taille(self) -> int:
        t: int = 0
        if any(issubclass(type(attr), C_Element) for attr in self.__dict__.values()):
            for attr in self.__dict__.values():
                if issubclass(type(attr), C_Element):
                    t += attr.taille
        else:
            raise AttributeError(f"Package {self.nom} ne contient aucun élément")
        return t

    @property
    def elements(self) -> list:
        return self._elements
