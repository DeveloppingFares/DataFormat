from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Enumerate import C_Enumerate
from Source.Data.Utilitaires.M_Constantes import E_Format


class C_EnumerateFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Enumerate:
        dependances = list()
        for dependance in kwargs["dependance"]:
            dependances.append(self.librairie.getFactory(E_Format.from_str("dependance")).creerDonnees(dependance))
        kwargs["dependance"] = dependances
        del kwargs["type_element"]
        return C_Enumerate(**kwargs)
