from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.M_Librairie import C_Librairie
from Source.Data.Format.M_Bitfield import C_Bitfield


class C_BitfieldFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Bitfield:
        elements = list()
        for element in kwargs["elements"]:
            elements.append(self.librairie.getFactory(element.get("type_element")).creerDonnees(**element))
        kwargs["elements"] = elements
        del kwargs["type_element"]
        return C_Bitfield(**kwargs)
