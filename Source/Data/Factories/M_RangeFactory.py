from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Range import C_Range
from Source.Data.Utilitaires.M_Constantes import E_Format
from Source.Data.Utilitaires.M_Utilitaires import extrait_attribut


class C_RangeFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Range:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        valeur = extrait_attribut(nom_attribut="valeur", type_attribut=str, contenu=kwargs, obligatoire=False)
        valeur = bytearray.fromhex(valeur) if valeur is not None else valeur
        taille = extrait_attribut(nom_attribut="taille", type_attribut=int, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)
        valeur_min = extrait_attribut(nom_attribut="valeur_min", type_attribut=int, contenu=kwargs)
        valeur_max = extrait_attribut(nom_attribut="valeur_max", type_attribut=int, contenu=kwargs)

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(self.librairie.getFactory(E_Format.from_str("dependance")).creerDonnees(dependance))

        return C_Range(nom=nom, description=description, dependance=dependances, taille=taille, valeur=valeur, valeur_min=valeur_min, valeur_max=valeur_max)
