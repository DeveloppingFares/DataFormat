from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Field import C_Field
from Source.Data.Utilitaires.M_Constantes import E_Format
from Source.Data.Utilitaires.M_Utitilaires import extrait_attribut


class C_FieldFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Field:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        valeur = int(extrait_attribut(nom_attribut="valeur", type_attribut=str, contenu=kwargs), 2)
        taille = extrait_attribut(nom_attribut="taille", type_attribut=int, contenu=kwargs)
        offset = extrait_attribut(nom_attribut="offset", type_attribut=int, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(self.librairie.getFactory(E_Format.from_str("dependance")).creerDonnees(dependance))

        return C_Field(nom=nom, description=description, dependance=dependances, taille=taille, offset=offset, valeur=valeur)
