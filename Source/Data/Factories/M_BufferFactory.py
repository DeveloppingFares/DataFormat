from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Buffer import C_Buffer


class C_BufferFactory(C_DonneesFactory):
    def creerDonnees(self, **kwargs) -> C_Buffer:
        return C_Buffer(**kwargs)
