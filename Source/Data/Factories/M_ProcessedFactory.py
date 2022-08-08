from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Processed import C_Processed


class C_ProcessedFactory(C_DonneesFactory):
    def creerDonnees(self, **kwargs) -> C_Processed:
        return C_Processed(**kwargs)
