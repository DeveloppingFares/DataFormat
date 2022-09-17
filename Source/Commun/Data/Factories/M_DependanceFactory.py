from Source.Commun.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Commun.Data.Format.M_Dependance import C_Dependance
from Source.Commun.Data.Utilitaires.M_Utilitaires import cherche_attribut


class C_DependanceFactory(C_DonneesFactory):
    def __init__(self, librairie, bloc):
        self.librairie = librairie
        self.bloc = bloc

    def creerDonnees(self, nom_dependance: str) -> C_Dependance:
        if nom_dependance is None:
            raise KeyError
        elif type(nom_dependance) != str:
            raise ValueError
        return C_Dependance(factory=self, nom_dependance=nom_dependance)

    def creerDonneesDepuisTemplate(self, template: C_Dependance) -> C_Dependance:
        raise NotImplementedError

    def cherche_dependance(self, nom_dependance: str):
        chemin_dependance = nom_dependance.split('.')
        if chemin_dependance[0].lower() == "volatile":
            return cherche_attribut(self.bloc, chemin_dependance[1:])
        elif chemin_dependance[0].lower() == "statique":
            return cherche_attribut(self.librairie, chemin_dependance[1:])
        else:
            raise NotImplementedError
