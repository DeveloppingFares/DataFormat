from Source.Commun.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Commun.Data.Factories.M_AbstractFactory import C_AbstractFactory
from Source.Commun.Data.Format.M_Field import C_Field
from Source.Commun.Data.Utilitaires.M_Constantes import E_Format
from Source.Commun.Data.Utilitaires.M_Utilitaires import extrait_attribut


class C_FieldFactory(C_DonneesFactory):
    def __init__(self, librairie, bloc):
        self.librairie = librairie
        self.bloc = bloc

    def creerDonnees(self, **kwargs) -> C_Field:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        valeur = extrait_attribut(nom_attribut="valeur", type_attribut=str, contenu=kwargs, obligatoire=False)
        valeur = int(valeur, 2) if valeur is not None else valeur
        taille = extrait_attribut(nom_attribut="taille", type_attribut=int, contenu=kwargs)
        offset = extrait_attribut(nom_attribut="offset", type_attribut=int, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)

        # Création nouvelle instance
        instance = C_Field(nom=nom, description=description, dependance=[], taille=taille, offset=offset, valeur=valeur)

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(C_AbstractFactory[E_Format.from_str("dependance")](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance))
        instance.ajout_dependances(dependances)

        return instance

    def creerDonneesDepuisTemplate(self, template: C_Field) -> C_Field:
        # Création nouvelle instance
        instance = C_Field(nom=template.nom, description=template.description, dependance=[], taille=template.taille, offset=template.offset, valeur=None)

        # Dependance
        dependances = list()
        for dependance in template.dependance:
            dependances.append(C_AbstractFactory[E_Format.from_str(dependance.type_element)](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance.nom_dependance))
        instance.ajout_dependances(dependances)

        return instance
