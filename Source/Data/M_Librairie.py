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


class C_Librairie(object):
    def __init__(self):
        pass

    def factoryJSON(self, filepath: str) -> C_Package | C_Bitfield | C_Enumerate | C_Field | C_Processed | C_Buffer | C_Range:
        if not os.path.isfile(filepath):
            raise FileNotFoundError
        with open(filepath) as f:
            dict_json = json.load(f)
        type_element = dict_json.get("type_element")
        if type_element is None:
            raise KeyError
        elif type_element == C_Donnees.type_donnees.package.value:
            return C_Package(**dict_json)


