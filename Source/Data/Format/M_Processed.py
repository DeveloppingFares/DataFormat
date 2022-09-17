import os
from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Element import C_Element


class C_Processed(C_observable, C_Element):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, processor: callable, entrants: list):
        self._processor: callable = processor
        self._entrants: list = entrants

        # Depuis Observable
        super().__init__()

        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

        # Depuis Element
        self._taille: int = taille

    @property
    def processor(self) -> str:
        return self._processor

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
        return 'processed'

    @property
    def dependance(self) -> list:
        return self._dependance

    @property
    def entrants(self) -> list:
        return self._entrants

    @property
    def random(self) -> bytearray:
        return bytearray(os.urandom(self.taille))

    def ajout_dependances(self, dependances: list):
        self._dependance = dependances

    def ajout_entrants(self, entrants: list):
        self._entrants = entrants

    # ==================================================================================================================
    # Depuis Observer
    # ==================================================================================================================
    def ajout_observer(self):
        for dependance in self.dependance:
            dependance.ajout_observer(self)

    def update(self, **kwargs) -> None:
        print(f"Ici {self.nom} qui dit: Salut les mioches!")

    # ==================================================================================================================
    # Depuis Element
    # ==================================================================================================================
    @property
    def valeur(self) -> bytearray:
        entrants = bytearray()
        for entrant in self._entrants:
            entrants += entrant.valeur
        processed = self._processor(entrants)
        self.notify()
        return processed

    @property
    def taille(self) -> int:
        return self._taille
