from Source.Commun.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Commun.Data.Factories.M_AbstractFactory import C_AbstractFactory
from Source.Commun.Data.Format.M_Buffer import C_Buffer
from Source.Commun.Data.Utilitaires.M_Constantes import E_Format
from Source.Commun.Data.Utilitaires.M_Utilitaires import extrait_attribut


class C_BufferFactory(C_DonneesFactory):
    def __init__(self, librairie, bloc):
        self.librairie = librairie
        self.bloc = bloc

    def creerDonnees(self, **kwargs) -> C_Buffer:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        valeur = extrait_attribut(nom_attribut="valeur", type_attribut=str, contenu=kwargs, obligatoire=False)
        valeur = bytearray.fromhex(valeur) if valeur is not None else valeur
        taille = extrait_attribut(nom_attribut="taille", type_attribut=int, contenu=kwargs, obligatoire=False)
        taille_variable = extrait_attribut(nom_attribut="taille_variable", type_attribut=str, contenu=kwargs, obligatoire=False)
        if taille is None and taille_variable is None:
            raise Exception("Un champ taille ou un champ taille_variable doivent etre définis pour les buffers")
        if taille is not None and taille_variable is not None:
            raise Exception("Les buffers ne peuvent pas contenir un champ taille et un champ taille variable")
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)

        # Création nouvelle instance
        if taille is not None:
            instance = C_Buffer(nom=nom, description=description, dependance=[], taille=taille, taille_variable=None, valeur=valeur)
        elif taille_variable is not None:
            instance = C_Buffer(nom=nom, description=description, dependance=[], taille=None, taille_variable=None, valeur=valeur)
            reference_taille_variable = C_AbstractFactory[E_Format.from_str("reference")](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom='taille_variable', nom_reference=taille_variable)
            instance.set_taille_variable_reference(reference_taille_variable)
        else:
            raise NotImplementedError

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(C_AbstractFactory[E_Format.from_str("dependance")](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance))
        instance.ajout_dependances(dependances)

        return instance

    def creerDonneesDepuisTemplate(self, template: C_Buffer) -> C_Buffer:
        # Création nouvelle instance
        if template.taille_variable is None:
            instance = C_Buffer(nom=template.nom, description=template.description, dependance=[], taille=template.taille, taille_variable=None, valeur=None)
        else:
            instance = C_Buffer(nom=template.nom, description=template.description, dependance=[], taille=None, taille_variable=None, valeur=None)
            reference_taille_variable = C_AbstractFactory[E_Format.from_str("reference")](self.librairie, instance if self.bloc is None else self.bloc).creerDonneesDepuisTemplate(template.taille_variable)
            instance.set_taille_variable_reference(reference_taille_variable)

        # Dependance
        dependances = list()
        for dependance in template.dependance:
            dependances.append(C_AbstractFactory[E_Format.from_str(dependance.type_element)](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance.nom_dependance))
        instance.ajout_dependances(dependances)

        return instance
