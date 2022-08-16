from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Buffer import C_Buffer
from Source.Data.Utilitaires.M_Utitilaires import extrait_attribut
from Source.Data.Utilitaires.M_Constantes import E_Format


class C_BufferFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Buffer:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        valeur = bytearray.fromhex(extrait_attribut(nom_attribut="valeur", type_attribut=str, contenu=kwargs))
        taille = extrait_attribut(nom_attribut="taille", type_attribut=int, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(self.librairie.getFactory(E_Format.from_str("dependance")).creerDonnees(dependance))

        return C_Buffer(nom=nom, description=description, dependance=dependances, taille=taille, valeur=valeur)
