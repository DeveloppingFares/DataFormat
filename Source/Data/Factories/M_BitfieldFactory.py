from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Bitfield import C_Bitfield


class C_BitfieldFactory(C_DonneesFactory):
    def creerDonnees(self, **kwargs) -> C_Bitfield:
        raise NotImplementedError
