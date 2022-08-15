from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Enumerate import C_Enumerate


class C_EnumerateFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Enumerate:
        del kwargs["type_element"]
        return C_Enumerate(**kwargs)
