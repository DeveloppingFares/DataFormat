from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Reference import C_Reference


class C_ReferenceFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs):
        nom = kwargs.get("nom")
        if nom is None:
            raise KeyError
        nom_reference = kwargs.get("nom_reference")
        if nom_reference is None:
            raise KeyError
        return C_Reference(factory=self, nom=nom, nom_reference=nom_reference)

    def cherche_reference(self, nom_reference: str):
        return self.librairie.cherche_attribut(nom_reference)
