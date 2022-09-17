from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Reference import C_Reference
from Source.Data.Utilitaires.M_Utilitaires import extrait_attribut, cherche_attribut


class C_ReferenceFactory(C_DonneesFactory):
    def __init__(self, librairie, bloc):
        self.librairie = librairie
        self.bloc = bloc

    def creerDonnees(self, **kwargs) -> C_Reference:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        nom_reference = extrait_attribut(nom_attribut="nom_reference", type_attribut=str, contenu=kwargs)
        return C_Reference(factory=self, nom=nom, nom_reference=nom_reference)

    def creerDonneesDepuisTemplate(self, template: C_Reference) -> C_Reference:
        return C_Reference(factory=self, nom=template.nom, nom_reference=template.nom_reference)

    def cherche_reference(self, nom_reference: str):
        chemin_reference = nom_reference.split('.')
        if chemin_reference[0].lower() == "volatile":
            return cherche_attribut(self.bloc, chemin_reference[1:])
        elif chemin_reference[0].lower() == "statique":
            return cherche_attribut(self.librairie, chemin_reference[1:])
        else:
            raise NotImplementedError
