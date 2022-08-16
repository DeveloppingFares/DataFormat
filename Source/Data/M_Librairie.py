import os
from Source.Data.Utilitaires.M_Constantes import E_Format
from Source.Data.Interfaces.M_Donnees import C_Donnees
from Source.Data.Factories.M_PackageFactory import C_PackageFactory
from Source.Data.Factories.M_BitfieldFactory import C_BitfieldFactory
from Source.Data.Factories.M_EnumerateFactory import C_EnumerateFactory
from Source.Data.Factories.M_FieldFactory import C_FieldFactory
from Source.Data.Factories.M_ProcessedFactory import C_ProcessedFactory
from Source.Data.Factories.M_BufferFactory import C_BufferFactory
from Source.Data.Factories.M_RangeFactory import C_RangeFactory
from Source.Data.Factories.M_ReferenceFactory import C_ReferenceFactory
from Source.Data.Factories.M_DependanceFactory import C_DependanceFactory
from Source.Data.Importer.M_FileImporter import C_FileImporter, C_ResultatImport


class C_Librairie(object):
    def __init__(self):
        pass

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
            setattr(self, resultat_import.nom, self.getFactory(resultat_import.format).creerDonnees(**resultat_import.contenu))

    def getFactory(self, format_element: str):
        if format_element == E_Format.package:
            return C_PackageFactory(self)
        elif format_element == E_Format.bitfield:
            return C_BitfieldFactory(self)
        elif format_element == E_Format.buffer:
            return C_BufferFactory(self)
        elif format_element == E_Format.enumerate:
            return C_EnumerateFactory(self)
        elif format_element == E_Format.processed:
            return C_ProcessedFactory(self)
        elif format_element == E_Format.range:
            return C_RangeFactory(self)
        elif format_element == E_Format.field:
            return C_FieldFactory(self)
        elif format_element == E_Format.reference:
            return C_ReferenceFactory(self)
        elif format_element == E_Format.dependance:
            return C_DependanceFactory(self)
        else:
            raise ValueError

    def cherche_attribut(self, chemin_attribut: str):
        objet = self
        liste_chemin = chemin_attribut.split('.')
        for attr in liste_chemin:
            if attr in objet.__dict__:
                objet = objet.__getattribute__(attr)
            else:
                return None
        return objet

    def ajout_observer(self):
        for attr in self.__dict__.values():
            if issubclass(type(attr), C_Donnees):
                attr.ajout_observer()
