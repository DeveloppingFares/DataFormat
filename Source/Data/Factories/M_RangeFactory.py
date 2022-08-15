from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Range import C_Range


class C_RangeFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Range:
        dependances = list()
        for dependance in kwargs["dependance"]:
            dependances.append(self.librairie.getFactory("dependance").creerDonnees(dependance))
        kwargs["dependance"] = dependances
        del kwargs["type_element"]
        return C_Range(**kwargs)
