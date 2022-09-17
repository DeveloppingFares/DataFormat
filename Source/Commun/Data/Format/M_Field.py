from Source.Commun.Observer.M_observable import C_observable
from Source.Commun.Data.Interfaces.M_Donnees import C_Donnees
from Source.Commun.Data.Corrupter.M_AbstractCorrupter import C_AbstractCorrupter
from Source.Commun.Data.Utilitaires.M_Constantes import E_Corruption
from random import randint


class C_Field(C_observable, C_Donnees):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, offset: int, valeur: int):
        self._offset: int = offset
        self._taille: int = taille
        self._masque: int = (0xFFFFFFFF >> (32 - self._taille)) << self._offset
        self._valeur: int = valeur if valeur is not None else self.random

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

    def _corrupt(self, type_corruption: str, **kwargs):
        return C_AbstractCorrupter[E_Corruption.from_str(type_corruption)].corrupt(self.valeur, **kwargs)

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
        return 'field'

    @property
    def dependance(self) -> list:
        return self._dependance

    @property
    def random(self) -> int:
        return randint(0, (1 << self._taille) - 1)

    def ajout_dependances(self, dependances: list):
        self._dependance = dependances

    # ==================================================================================================================
    # Depuis Observer
    # ==================================================================================================================
    def ajout_observer(self):
        for dependance in self.dependance:
            dependance.ajout_observer(self)

    def update(self, **kwargs) -> None:
        print(f"Notification de {self.nom} depuis {kwargs.get('nom_emetteur')} ({kwargs.get('type_emetteur')})")

    def randomize(self):
        self.valeur = self.random

    def __str__(self):
        return f"""{self.nom}: {self.valeur:0{self.taille}b}
\tType: {str(type(self))}
\tDescription: {self.description}
\tTaille: {str(self.taille)} bits
"""
