import os
import random
from enum import Enum
from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Element import C_Element


class C_Enumerate(C_observable, C_Element):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, valeurs: Enum, defaut: str):
        self._valeurs: Enum = valeurs
        self._defaut: str = defaut
        self._valeur: bytearray = self.get_enum_from_str(self._defaut)

        # Depuis Observable
        super().__init__()

        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

        # Depuis Element
        self._taille: int = taille

    def get_enum_from_str(self, nom_enum: str) -> bytearray:
        for nom, valeur in self._valeurs.__members__.items():
            if nom_enum == nom:
                return valeur.value
        raise KeyError(f"L'enumere ne contient pas de membre appelé {nom_enum}")

    def is_value_in_enum(self, value: bytearray) -> bool:
        for nom, valeur in self._valeurs.__members__.items():
            if value == valeur.value:
                return True
        return False

    @property
    def valeurs(self) -> Enum:
        return self._valeurs

    @property
    def defaut(self) -> str:
        return self._defaut

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
        return 'enumerate'

    @property
    def dependance(self) -> list:
        return self._dependance

    @property
    def random(self) -> bytearray:
        return random.choice(list(self._valeurs.__members__.values())).value

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

    # ==================================================================================================================
    # Depuis Element
    # ==================================================================================================================
    @property
    def valeur(self) -> bytearray:
        return self._valeur

    @valeur.setter
    def valeur(self, v: bytearray):
        if not self.is_value_in_enum(v):
            raise ValueError(f"Valeur d'initialisation {v.hex()} de l'enumere {self.nom} incohérente")
        self._valeur = v
        self.notify()

    @property
    def taille(self) -> int:
        return self._taille
