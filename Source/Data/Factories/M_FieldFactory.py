from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Field import C_Field


class C_FieldFactory(C_DonneesFactory):
    def creerDonnees(self, **kwargs) -> C_Field:
        return C_Field(**kwargs)
