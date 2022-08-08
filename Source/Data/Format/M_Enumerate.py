import os
from Source.Data.Interfaces.M_Element import C_Element


class C_Enumerate(C_Element):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, valeur: bytearray):
        if len(valeur) != taille:
            raise ValueError(f"Taille de la valeur d'initialisation de l'enumerate {nom} incohérente")
        self._valeur: bytearray = valeur

        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

        # Depuis Element
        self._taille: int = taille

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
    # Depuis Element
    # ==================================================================================================================
    @property
    def valeur(self) -> bytearray:
        return self._valeur

    @valeur.setter
    def valeur(self, v: bytearray):
        if len(v) != self.taille:
            raise ValueError(f"Taille de la valeur d'initialisation du buffer {self.nom} incohérente")
        self._valeur = v

    @property
    def taille(self) -> int:
        return self._taille
