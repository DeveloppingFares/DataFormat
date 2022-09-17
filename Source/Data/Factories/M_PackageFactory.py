from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Factories.M_AbstractFactory import C_AbstractFactory
from Source.Data.Format.M_Package import C_Package
from Source.Data.Utilitaires.M_Constantes import E_Format
from Source.Data.Utilitaires.M_Utilitaires import extrait_attribut


class C_PackageFactory(C_DonneesFactory):
    def __init__(self, librairie, bloc):
        self.librairie = librairie
        self.bloc = bloc

    def creerDonnees(self, **kwargs) -> C_Package:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        input_elements = extrait_attribut(nom_attribut="elements", type_attribut=list, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)

        # Création nouvelle instance
        instance = C_Package(nom=nom, description=description, dependance=[], elements=[])

        # Elements
        elements = list()
        for element in input_elements:
            type_element = extrait_attribut(nom_attribut="type_element", type_attribut=str, contenu=element)
            elements.append(
                C_AbstractFactory[E_Format.from_str(type_element)](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(**element))
        instance.ajout_elements(elements)

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(C_AbstractFactory[E_Format.from_str("dependance")](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance))
        instance.ajout_dependances(dependances)

        return instance

    def creerDonneesDepuisTemplate(self, template: C_Package) -> C_Package:
        # Création nouvelle instance
        instance = C_Package(nom=template.nom, description=template.description, dependance=[], elements=[])

        # Elements
        elements = list()
        for element in template.elements:
            elements.append(C_AbstractFactory[E_Format.from_str(element.type_element)](self.librairie, instance if self.bloc is None else self.bloc).creerDonneesDepuisTemplate(element))
        instance.ajout_elements(elements)

        # Dependance
        dependances = list()
        for dependance in template.dependance:
            dependances.append(C_AbstractFactory[E_Format.from_str(dependance.type_element)](self.librairie, instance if self.bloc is None else self.bloc).creerDonnees(nom_dependance=dependance.nom_dependance))
        instance.ajout_dependances(dependances)

        return instance
