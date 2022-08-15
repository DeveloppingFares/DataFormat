from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Field import C_Field


class C_FieldFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Field:
        del kwargs["type_element"]
        kwargs["valeur"] = int(kwargs.get("valeur"), 2)
        return C_Field(**kwargs)
