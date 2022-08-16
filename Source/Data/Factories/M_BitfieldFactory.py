from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Bitfield import C_Bitfield
from Source.Data.Utilitaires.M_Utitilaires import extrait_attribut
from Source.Data.Utilitaires.M_Constantes import E_Format


class C_BitfieldFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Bitfield:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        input_elements = extrait_attribut(nom_attribut="elements", type_attribut=list, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)

        # Elements
        elements = list()
        for element in input_elements:
            elements.append(self.librairie.getFactory(E_Format.from_str(element.get("type_element"))).creerDonnees(**element))

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(self.librairie.getFactory(E_Format.from_str("dependance")).creerDonnees(dependance))

        return C_Bitfield(nom=nom, description=description, dependance=dependances, elements=elements)
