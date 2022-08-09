from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Range import C_Range


class C_RangeFactory(C_DonneesFactory):
    def creerDonnees(self, **kwargs) -> C_Range:
        del kwargs["type_element"]
        return C_Range(**kwargs)
