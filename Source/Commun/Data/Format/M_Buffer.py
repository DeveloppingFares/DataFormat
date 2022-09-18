import os
from Source.Commun.Observer.M_observable import C_observable
from Source.Commun.Data.Interfaces.M_Element import C_Element
from Source.Commun.Data.Format.M_Reference import C_Reference
from Source.Commun.Data.Format.M_Range import C_Range
from Source.Commun.Data.Format import ErreurValeurHorsLimite


class C_Buffer(C_observable, C_Element):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, taille_variable: C_Reference, valeur: bytearray):
        # Depuis Observable
        super().__init__()

        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

        # Depuis Element
        self._taille: int = taille
        self._taille_variable: C_Reference = taille_variable

        # Specifique
        self._valeur = None
        if self._taille is not None:
            self.valeur: bytearray = valeur if valeur is not None else self.random

    @property
    def taille_variable(self) -> C_Reference:
        if self._taille_variable is not None:
            if type(self._taille_variable.reference) != C_Range:
                raise TypeError("La reference doit pointer vers une variable de type range")
        return self._taille_variable

    def set_taille_variable_reference(self, reference: C_Reference):
        self._taille_variable = reference

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
        return 'buffer'

    @property
    def dependance(self) -> list:
        return self._dependance

    @property
    def random(self) -> bytearray:
        return bytearray(os.urandom(self.taille))

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
        if self._valeur is None:
            self.randomize()
        return self._valeur

    @valeur.setter
    def valeur(self, v: bytearray):
        if len(v) != self.taille:
            raise ErreurValeurHorsLimite(nom_attribut=self.nom, taille_attendue=self.taille, taille_fournie=len(v))
        self._valeur = v
        self.notify()

    @property
    def taille(self) -> int:
        return self._taille if self._taille is not None else self.taille_variable.reference.valeur_entiere
