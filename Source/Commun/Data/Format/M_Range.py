from random import randint
from Source.Commun.Observer.M_observable import C_observable
from Source.Commun.Data.Interfaces.M_Element import C_Element


class C_Range(C_observable, C_Element):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, valeur: int, valeur_min: int, valeur_max: int):
        self._valeur_min: int = valeur_min
        self._valeur_max: int = valeur_max
        self._valeur: int = int()

        # Depuis Observable
        super().__init__()

        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

        # Depuis Element
        self._taille: int = taille
        self.valeur = valeur if valeur is not None else self.random

    @property
    def valeur_min(self) -> int:
        return self._valeur_min

    @property
    def valeur_max(self) -> int:
        return self._valeur_max

    @property
    def valeur_entiere(self) -> int:
        return self._valeur

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
        return 'range'

    @property
    def dependance(self) -> list:
        return self._dependance

    @property
    def random(self) -> bytearray:
        return bytearray(randint(self._valeur_min, self._valeur_max).to_bytes(self.taille, 'big'))

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
        return bytearray(self._valeur.to_bytes(self.taille, 'big'))

    @valeur.setter
    def valeur(self, v):
        if isinstance(v, bytearray):
            if len(v) != self.taille:
                raise ValueError(f"Taille de la valeur d'initialisation du range {self.nom} incohérente")
            v_int = int.from_bytes(v, 'big')
        elif isinstance(v, int):
            v_int = v
        else:
            raise TypeError(f"Type de données non prises en compte")

        if self._valeur_min <= v_int <= self._valeur_max:
            self._valeur = v_int
        else:
            raise ValueError(f"Valeur hors des limites définies pour le range {self.nom}")
        self.notify()

    @property
    def taille(self) -> int:
        return self._taille
