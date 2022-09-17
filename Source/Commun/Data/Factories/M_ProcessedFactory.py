from Source.Commun.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Commun.Data.Factories.M_AbstractFactory import C_AbstractFactory
from Source.Commun.Data.Format.M_Processed import C_Processed
from Source.Commun.Data.Utilitaires.M_Constantes import E_Format
from Source.Commun.Data.Utilitaires.M_Utilitaires import extrait_attribut


class C_ProcessedFactory(C_DonneesFactory):
    def __init__(self, librairie, bloc):
        self.librairie = librairie
        self.bloc = bloc

    def creerDonnees(self, **kwargs) -> C_Processed:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        taille = extrait_attribut(nom_attribut="taille", type_attribut=int, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)
        processor = self.librairie.get_formatter(extrait_attribut(nom_attribut="processor", type_attribut=str, contenu=kwargs))
        input_entrants = extrait_attribut(nom_attribut="entrant", type_attribut=list, contenu=kwargs)

        # Création nouvelle instance
        instance = C_Processed(nom=nom, description=description, dependance=[], taille=taille, processor=processor, entrants=[])

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(C_AbstractFactory[E_Format.from_str("dependance")](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance))
        instance.ajout_dependances(dependances)

        # Entrants
        entrants = list()
        for entrant in input_entrants:
            entrants.append(C_AbstractFactory[E_Format.from_str("reference")](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom=entrant, nom_reference=entrant))
        instance.ajout_entrants(entrants)

        return instance

    def creerDonneesDepuisTemplate(self, template: C_Processed) -> C_Processed:
        # Création nouvelle instance
        instance = C_Processed(nom=template.nom, description=template.description, dependance=[], taille=template.taille, processor=template.processor, entrants=[])

        # Dependance
        dependances = list()
        for dependance in template.dependance:
            dependances.append(C_AbstractFactory[E_Format.from_str(dependance.type_element)](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance.nom_dependance))
        instance.ajout_dependances(dependances)

        # Entrants
        entrants = list()
        for entrant in template.entrants:
            entrants.append(C_AbstractFactory[E_Format.from_str("reference")](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom=entrant.nom, nom_reference=entrant.nom))
        instance.ajout_entrants(entrants)

        return instance
