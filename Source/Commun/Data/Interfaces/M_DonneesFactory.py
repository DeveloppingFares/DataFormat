from Source.Commun.Data.Interfaces.M_Donnees import C_Donnees
from abc import ABCMeta, abstractmethod


class C_DonneesFactory(metaclass=ABCMeta):
    @abstractmethod
    def creerDonnees(self, **kwargs) -> C_Donnees:
        raise NotImplementedError

    @abstractmethod
    def creerDonneesDepuisTemplate(self, template: C_Donnees) -> C_Donnees:
        raise NotImplementedError
