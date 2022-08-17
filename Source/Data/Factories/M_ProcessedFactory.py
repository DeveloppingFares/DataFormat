from Source.Data.Interfaces.M_DonneesFactory import C_DonneesFactory
from Source.Data.Format.M_Processed import C_Processed
from Source.Data.Utilitaires.M_Constantes import E_Format
from Source.Data.Utilitaires.M_Utitilaires import extrait_attribut


class C_ProcessedFactory(C_DonneesFactory):
    def __init__(self, librairie):
        self.librairie = librairie

    def creerDonnees(self, **kwargs) -> C_Processed:
        nom = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        description = extrait_attribut(nom_attribut="description", type_attribut=str, contenu=kwargs)
        taille = extrait_attribut(nom_attribut="taille", type_attribut=int, contenu=kwargs)
        input_dependances = extrait_attribut(nom_attribut="dependance", type_attribut=list, contenu=kwargs)
        processor = self.librairie.get_formatter(extrait_attribut(nom_attribut="processor", type_attribut=str, contenu=kwargs))
        input_entrants = extrait_attribut(nom_attribut="entrant", type_attribut=list, contenu=kwargs)

        # Dependance
        dependances = list()
        for dependance in input_dependances:
            dependances.append(self.librairie.getFactory(E_Format.from_str("dependance")).creerDonnees(dependance))

        # Entrants
        entrants = list()
        for entrant in input_entrants:
            entrants.append(self.librairie.getFactory(E_Format.from_str("reference")).creerDonnees(nom=entrant, nom_reference=entrant))

        return C_Processed(nom=nom, description=description, dependance=dependances, taille=taille, processor=processor, entrants=entrants)
