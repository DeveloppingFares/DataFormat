import os
from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Element import C_Element
from Source.Data.Interfaces.M_Bloc import C_Bloc


class C_Reference(C_observable, C_Element):
    def __init__(self, factory, nom: str, nom_reference: str, reference: C_Element = None):
        self._reference: C_Element = reference
        self._nom_reference: str = nom_reference
        self.factory = factory

        # Depuis Observable
        super().__init__()

        # Depuis Donnees
        self._nom: str = nom
        self._description = None  # Inutilisé
        self._dependance = None  # Inutilisé

        # Depuis Element
        self._taille = None  # Inutilisé

    def chargement_reference(self):
        if self._reference is None:
            self._reference = self.factory.cherche_reference(nom_reference=self._nom_reference)
            if self._reference is None:
                raise AttributeError(f"Attribut {self._nom_reference} introuvable dans la librairie")
            if not issubclass(type(self._reference), C_Element) and not issubclass(type(self._reference), C_Bloc):
                raise TypeError(f"L'attribut {self._nom_reference} n'est ni un Element ni un Bloc")

    # ==================================================================================================================
    # Depuis Donnees
    # ==================================================================================================================
    @property
    def nom(self) -> str:
        return self._nom

    @property
    def description(self) -> str:
        self.chargement_reference()
        return self._reference.description

    @property
    def dependance(self) -> list:
        self.chargement_reference()
        return self._reference.dependance

    @property
    def random(self) -> bytearray:
        self.chargement_reference()
        return self._reference.random

    def update(self, **kwargs) -> None:
        self.chargement_reference()
        raise NotImplementedError

    # ==================================================================================================================
    # Depuis Element
    # ==================================================================================================================
    @property
    def valeur(self) -> bytearray:
        self.chargement_reference()
        return self._reference.valeur

    @valeur.setter
    def valeur(self, v: bytearray):
        self.chargement_reference()
        self._reference.valeur = v

    @property
    def taille(self) -> int:
        self.chargement_reference()
        return self._reference.taille
