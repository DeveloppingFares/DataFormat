import os
from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Element import C_Element
from Source.Data.Format import ErreurValeurHorsLimite


class C_Buffer(C_observable, C_Element):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, valeur: bytearray):
        # Depuis Observable
        super().__init__()

        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

        # Depuis Element
        self._taille: int = taille

        # Specifique
        self._valeur: bytearray = valeur if valeur is not None else self.random

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
        nouvelle_instance = C_Buffer(nom=self._nom,
                                     description=self._description,
                                     dependance=list(map(lambda x: x.factory(), self._dependance)),
                                     taille=self._taille,
                                     valeur=None)
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
        return self._valeur

    @valeur.setter
    def valeur(self, v: bytearray):
        if len(v) != self.taille:
            raise ErreurValeurHorsLimite(nom_attribut=self.nom, taille_attendue=self.taille, taille_fournie=len(v))
        self._valeur = v
        self.notify()

    @property
    def taille(self) -> int:
        return self._taille
