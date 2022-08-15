from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Dependance import C_Dependance


class C_DependanceFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, nom_dependance: str):
        if nom_dependance is None:
            raise KeyError
        return C_Dependance(factory=self, nom_dependance=nom_dependance)

    def cherche_dependance(self, nom_dependance: str):
        return self.librairie.cherche_attribut(nom_dependance)
