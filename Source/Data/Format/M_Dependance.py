from Source.Observer.M_observable import C_observable
from Source.Observer.M_observer import C_observer


class C_Dependance:
    def __init__(self, factory, nom_dependance: str, dependance=None):
        self._dependance: C_observable = dependance
        self._nom_dependance: str = nom_dependance
        self.factory = factory

    def chargement_dependance(self):
        if self._dependance is None:
            self._dependance = self.factory.cherche_dependance(nom_dependance=self._nom_dependance)
            if self._dependance is None:
                raise AttributeError(f"Attribut {self._nom_dependance} introuvable dans la librairie")
            if not isinstance(self._dependance, C_observable):
                raise TypeError(f"L'attribut {self._nom_dependance} n'est pas une Donnees")

    # ==================================================================================================================
    # Depuis Observable
    # ==================================================================================================================
    def ajout_observer(self, observer: C_observer):
        self.chargement_dependance()
        if not issubclass(type(observer), C_observer):
            raise TypeError
        self._dependance.add_observer(observer)
