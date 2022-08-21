from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Donnees import C_Donnees
from random import randint


class C_Field(C_observable, C_Donnees):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, offset: int, valeur: int):
        self._valeur: int = valeur
        self._offset: int = offset
        self._taille: int = taille
        self._masque: int = (0xFFFFFFFF >> (32 - self._taille)) << self._offset

        # Depuis Observable
        super().__init__()

        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

    @property
    def valeur(self) -> int:
        return self._valeur

    @valeur.setter
    def valeur(self, v: int):
        self._valeur = v
        self.notify()

    @property
    def offset(self) -> int:
        return self._offset

    @property
    def masque(self) -> int:
        return self._masque

    @property
    def taille(self) -> int:
        return self._taille

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
    def random(self) -> int:
        return randint(0, (1 << self._taille) - 1)

    # ==================================================================================================================
    # Depuis Observer
    # ==================================================================================================================
    def ajout_observer(self):
        for dependance in self.dependance:
            dependance.ajout_observer(self)

    def update(self, **kwargs) -> None:
        raise NotImplementedError

    def randomize(self):
        self.valeur = self.random

    def __str__(self):
        return f"""{self.nom}: {self.valeur:b}
\tType: {str(type(self))}
\tDescription: {self.description}
\tTaille: {str(self.taille)} bits
"""
