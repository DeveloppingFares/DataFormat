import os
from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Element import C_Element


class C_Processed(C_observable, C_Element):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, processor: callable):
        self._processor = processor

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
        return self._processor()

    @property
    def taille(self) -> int:
        return self._taille