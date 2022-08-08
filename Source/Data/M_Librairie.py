import json
import os
from Source.Data.Interfaces.M_Donnees import C_Donnees
from Source.Data.Format.M_Package import C_Package
from Source.Data.Format.M_Bitfield import C_Bitfield
from Source.Data.Format.M_Enumerate import C_Enumerate
from Source.Data.Format.M_Field import C_Field
from Source.Data.Format.M_Processed import C_Processed
from Source.Data.Format.M_Buffer import C_Buffer
from Source.Data.Format.M_Range import C_Range
from Source.Data.Factories.M_PackageFactory import C_PackageFactory
from Source.Data.Factories.M_BitfieldFactory import C_BitfieldFactory
from Source.Data.Factories.M_EnumerateFactory import C_EnumerateFactory
from Source.Data.Factories.M_FieldFactory import C_FieldFactory
from Source.Data.Factories.M_ProcessedFactory import C_ProcessedFactory
from Source.Data.Factories.M_BufferFactory import C_BufferFactory
from Source.Data.Factories.M_RangeFactory import C_RangeFactory


class C_Librairie(object):
    def __init__(self):
        pass

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

    @staticmethod
    def getFactory(type_element: str):
        if type_element == C_Donnees.type_donnees.package.value:
            return C_PackageFactory()
        elif type_element == C_Donnees.type_donnees.bitfield.value:
            return C_BitfieldFactory()
        elif type_element == C_Donnees.type_donnees.buffer.value:
            return C_BufferFactory()
        elif type_element == C_Donnees.type_donnees.enumerate.value:
            return C_EnumerateFactory()
        elif type_element == C_Donnees.type_donnees.processed.value:
            return C_ProcessedFactory()
        elif type_element == C_Donnees.type_donnees.range.value:
            return C_RangeFactory()
        elif type_element == C_Donnees.type_donnees.field.value:
            return C_FieldFactory()
        else:
            raise ValueError
