import os
import json
from Source.Data.M_Package import C_donnees
from Source.Data.M_Bitfield import C_bitfield


def importJson(dirPath: str):
    for root, dirs, files in os.walk(r"/TestData"):
        for f in files:

        importJson(os.path.join(root, dirs, files))

if __name__ == '__main__':
    for root, dirs, files in os.walk(r"/TestData"):
        importJson(os.path.join(root, dirs, files))
    with open(r"/TestData/donnees.json") as f:
        myRaw = C_donnees(nom="package", dependance=[])
        myRaw.importJSON(json.load(f))
    with open(r"/TestData/bitfield.json") as f:
        myBitfield = C_bitfield(nom="bitfield", dependance=[])
        myBitfield.importJSON(json.load(f))
    print("test")
