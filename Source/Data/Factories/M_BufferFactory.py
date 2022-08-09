from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Buffer import C_Buffer


class C_BufferFactory(C_DonneesFactory):
    def creerDonnees(self, **kwargs) -> C_Buffer:
        kwargs["valeur"] = bytearray.fromhex(kwargs.get("valeur"))
        del kwargs["type_element"]
        return C_Buffer(**kwargs)
