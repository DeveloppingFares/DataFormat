from enum import Enum
from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Enumerate import C_Enumerate
from Source.Data.Utilitaires.M_Utitilaires import extrait_attribut
from Source.Data.Utilitaires.M_Constantes import E_Format


class C_EnumerateFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Enumerate:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        input_valeurs = extrait_attribut(nom_attribut="enum", type_attribut=dict, contenu=kwargs)
        taille = extrait_attribut(nom_attribut="taille", type_attribut=int, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)
        defaut = extrait_attribut(nom_attribut="defaut", type_attribut=str, contenu=kwargs)

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(self.librairie.getFactory(E_Format.from_str("dependance")).creerDonnees(dependance))

        # Valeurs
        for k, v in input_valeurs.items():
            input_valeurs[k] = bytearray.fromhex(v)
        valeurs = Enum(nom, input_valeurs)

        return C_Enumerate(nom=nom, description=description, dependance=dependances, taille=taille, valeurs=valeurs, defaut=defaut)
