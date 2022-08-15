from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.M_Librairie import C_Librairie
from Source.Data.Format.M_Package import C_Package


class C_PackageFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Package:
        elements = list()
        for element in kwargs["elements"]:
            elements.append(self.librairie.getFactory(element.get("type_element")).creerDonnees(**element))
        kwargs["elements"] = elements
        dependances = list()
        for dependance in kwargs["dependance"]:
            dependances.append(self.librairie.getFactory("dependance").creerDonnees(dependance))
        kwargs["dependance"] = dependances
        del kwargs["type_element"]
        return C_Package(**kwargs)
