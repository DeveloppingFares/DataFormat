import os
from Source.Commun.Data.Utilitaires.M_Constantes import E_Format
from Source.Commun.Data.Interfaces.M_Donnees import C_Donnees
from Source.Commun.Data.Factories.M_AbstractFactory import C_AbstractFactory
from Source.Specifique.Importer.M_FileImporter import C_FileImporter, C_ResultatImport
from Source.Specifique.Formatter.M_crc_A_32 import C_crc_A_32


class C_Librairie(object):
    def __init__(self):
        # Formatters
        self.crc_A_32 = C_crc_A_32()

    def importDirectory(self, dirpath: str):
        if not os.path.isdir(dirpath):
            raise FileNotFoundError
        for root, dirs, files in os.walk(dirpath):
            for f in files:
                self.factory(C_FileImporter(os.path.join(root, f)).import_file())
        self.ajout_observer()

    def factory(self, resultat_import: C_ResultatImport):
        if hasattr(self, resultat_import.nom):
            raise AttributeError(f"La librairie contient déjà une donnée appelée {resultat_import.nom}")
        else:
            setattr(self, resultat_import.nom, C_AbstractFactory[resultat_import.format](self, None).creerDonnees(**resultat_import.contenu))

    def ajout_observer(self):
        for attr in self.__dict__.values():
            if issubclass(type(attr), C_Donnees):
                attr.ajout_observer()

    def get_formatter(self, nom: str):
        if not hasattr(self, nom):
            raise AttributeError
        return self.__getattribute__(nom)

    def instancie(self, template: C_Donnees):
        instance = C_AbstractFactory[E_Format.from_str(template.type_element)](self, None).creerDonneesDepuisTemplate(template)
        instance.ajout_observer()
        return instance
