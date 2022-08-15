import json
import os
from enum import Enum
from Source.Data.Interfaces.M_Donnees import C_Donnees
from Source.Data.Format.M_Package import C_Package
from Source.Data.Format.M_Bitfield import C_Bitfield
from Source.Data.Format.M_Enumerate import C_Enumerate
from Source.Data.Format.M_Field import C_Field
from Source.Data.Format.M_Processed import C_Processed
from Source.Data.Format.M_Buffer import C_Buffer
from Source.Data.Format.M_Range import C_Range
from Source.Data.Factories.M_EnumerateFactory import C_EnumerateFactory
from Source.Data.Factories.M_FieldFactory import C_FieldFactory
from Source.Data.Factories.M_ProcessedFactory import C_ProcessedFactory
from Source.Data.Factories.M_BufferFactory import C_BufferFactory
from Source.Data.Factories.M_RangeFactory import C_RangeFactory
from Source.Data.Factories.M_ReferenceFactory import C_ReferenceFactory
from Source.Data.Factories.M_DependanceFactory import C_DependanceFactory


class C_Librairie(object):
    class type_donnees(Enum):
        bitfield = "bitfield"
        buffer = "buffer"
        enumerate = "enumerate"
        field = "field"
        package = "package"
        processed = "processed"
        range = "range"
        reference = "reference"
        dependance = "dependance"

    def __init__(self):
        pass

    def importDirectory(self, dirpath: str):
        if not os.path.isdir(dirpath):
            raise FileNotFoundError
        for root, dirs, files in os.walk(dirpath):
            for f in files:
                self.importJSON(os.path.join(root, f))

    def importJSON(self, filepath: str) -> C_Package | C_Bitfield | C_Enumerate | C_Field | C_Processed | C_Buffer | C_Range:
        if not os.path.isfile(filepath):
            raise FileNotFoundError
        with open(filepath) as f:
            dict_json = json.load(f)
        return self.factory(**dict_json)

    def factory(self, **kwargs) -> C_Package | C_Bitfield | C_Enumerate | C_Field | C_Processed | C_Buffer | C_Range:
        nom_element = kwargs.get("nom")
        if nom_element is None:
            raise KeyError
        type_element = kwargs.get("type_element")
        if type_element is None:
            raise KeyError

        if hasattr(self, nom_element):
            raise AttributeError
        else:
            setattr(self, nom_element, self.getFactory(type_element).creerDonnees(**kwargs))
        return self.__getattribute__(nom_element)

    def getFactory(self, type_element: str):
        if type_element == C_Librairie.type_donnees.package.value:
            from Source.Data.Factories.M_PackageFactory import C_PackageFactory
            return C_PackageFactory(self)
        elif type_element == C_Librairie.type_donnees.bitfield.value:
            from Source.Data.Factories.M_BitfieldFactory import C_BitfieldFactory
            return C_BitfieldFactory(self)
        elif type_element == C_Librairie.type_donnees.buffer.value:
            return C_BufferFactory(self)
        elif type_element == C_Librairie.type_donnees.enumerate.value:
            return C_EnumerateFactory(self)
        elif type_element == C_Librairie.type_donnees.processed.value:
            return C_ProcessedFactory(self)
        elif type_element == C_Librairie.type_donnees.range.value:
            return C_RangeFactory(self)
        elif type_element == C_Librairie.type_donnees.field.value:
            return C_FieldFactory(self)
        elif type_element == C_Librairie.type_donnees.reference.value:
            return C_ReferenceFactory(self)
        elif type_element == C_Librairie.type_donnees.dependance.value:
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
