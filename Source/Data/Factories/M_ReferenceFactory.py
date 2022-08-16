from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Reference import C_Reference
from Source.Data.Utilitaires.M_Utitilaires import extrait_attribut


class C_ReferenceFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Reference:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        nom_reference = extrait_attribut(nom_attribut="nom_reference", type_attribut=str, contenu=kwargs)
        return C_Reference(factory=self, nom=nom, nom_reference=nom_reference)

    def cherche_reference(self, nom_reference: str):
        return self.librairie.cherche_attribut(nom_reference)
