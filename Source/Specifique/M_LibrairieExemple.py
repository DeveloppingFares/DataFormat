import os
from Source.Commun.Data.Interfaces.M_Librairie import C_Librairie
from Source.Commun.Data.Factories.M_AbstractFactory import C_AbstractFactory
from Source.Specifique.Importer.M_FileImporter import C_FileImporter, C_ResultatImport
from Source.Specifique.Formatter.M_crc_A_32 import C_crc_A_32


class C_LibrairieExemple(C_Librairie):
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
