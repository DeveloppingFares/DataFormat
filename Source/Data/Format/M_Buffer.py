import os
from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Element import C_Element


class C_Buffer(C_observable, C_Element):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, valeur: bytearray):
        if len(valeur) != taille:
            raise ValueError(f"Taille de la valeur d'initialisation du buffer {nom} incohérente")
        self._valeur: bytearray = valeur

        # Depuis Observable
        super().__init__()

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

    def update(self, **kwargs) -> None:
        raise NotImplementedError

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
