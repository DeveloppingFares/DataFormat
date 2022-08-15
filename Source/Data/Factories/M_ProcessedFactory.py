from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Processed import C_Processed


class C_ProcessedFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Processed:
        del kwargs["type_element"]
        return C_Processed(**kwargs)
