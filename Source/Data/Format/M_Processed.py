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

    def factory(self):
        nouvelle_instance = C_Processed(nom=self._nom,
                                        description=self._description,
                                        dependance=list(map(lambda x: x.factory(), self._dependance)),
                                        taille=self._taille,
                                        processor=self._processor,
                                        entrants=self._entrants)
        nouvelle_instance.ajout_observer()
        return nouvelle_instance

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
