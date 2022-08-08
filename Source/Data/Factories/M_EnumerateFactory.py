from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Enumerate import C_Enumerate


class C_EnumerateFactory(C_DonneesFactory):
    def creerDonnees(self, **kwargs) -> C_Enumerate:
        return C_Enumerate(**kwargs)
