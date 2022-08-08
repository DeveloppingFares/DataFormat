from Source.Data.M_Librairie import C_Librairie
from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Package import C_Package


class C_PackageFactory(C_DonneesFactory):
    def creerDonnees(self, **kwargs) -> C_Package:
        elements = list()
        for element in kwargs["elements"]:
            elements.append(C_Librairie.getFactory(element.get("type_element")).creerDonnees(**element))
        kwargs["elements"] = elements
        return C_Package(**kwargs)
