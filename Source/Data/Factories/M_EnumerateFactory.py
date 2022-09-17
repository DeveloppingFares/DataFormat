from enum import Enum
from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Factories.M_AbstractFactory import C_AbstractFactory
from Source.Data.Format.M_Enumerate import C_Enumerate
from Source.Data.Utilitaires.M_Constantes import E_Format
from Source.Data.Utilitaires.M_Utilitaires import extrait_attribut


class C_EnumerateFactory(C_DonneesFactory):
    def __init__(self, librairie, bloc):
        self.librairie = librairie
        self.bloc = bloc

    def creerDonnees(self, **kwargs) -> C_Enumerate:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        input_valeurs = extrait_attribut(nom_attribut="enum", type_attribut=dict, contenu=kwargs)
        taille = extrait_attribut(nom_attribut="taille", type_attribut=int, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)
        defaut = extrait_attribut(nom_attribut="defaut", type_attribut=str, contenu=kwargs)

        # Valeurs
        for k, v in input_valeurs.items():
            input_valeurs[k] = bytearray.fromhex(v)
        valeurs = Enum(nom, input_valeurs)

        # Création nouvelle instance
        instance = C_Enumerate(nom=nom, description=description, dependance=[], taille=taille, valeurs=valeurs, defaut=defaut)

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(C_AbstractFactory[E_Format.from_str("dependance")](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance))
        instance.ajout_dependances(dependances)

        return instance

    def creerDonneesDepuisTemplate(self, template: C_Enumerate) -> C_Enumerate:
        # Création nouvelle instance
        instance = C_Enumerate(nom=template.nom, description=template.description, dependance=[], taille=template.taille, valeurs=template.valeurs, defaut=template.defaut)

        # Dependance
        dependances = list()
        for dependance in template.dependance:
            dependances.append(C_AbstractFactory[E_Format.from_str(dependance.type_element)](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance.nom_dependance))
        instance.ajout_dependances(dependances)

        return instance
