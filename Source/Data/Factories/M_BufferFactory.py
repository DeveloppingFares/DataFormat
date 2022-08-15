from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Buffer import C_Buffer


class C_BufferFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Buffer:
        kwargs["valeur"] = bytearray.fromhex(kwargs.get("valeur"))
        dependances = list()
        for dependance in kwargs["dependance"]:
            dependances.append(self.librairie.getFactory("dependance").creerDonnees(dependance))
        kwargs["dependance"] = dependances
        del kwargs["type_element"]
        return C_Buffer(**kwargs)
