from Source.Data.Interfaces.M_Donnees import C_Donnees
from abc import ABCMeta, abstractmethod


class C_DonneesFactory(metaclass=ABCMeta):
    @abstractmethod
    def creerDonnees(self, **kwargs) -> C_Donnees:
        raise NotImplementedError
