import os
import json
from Source.Data.M_Librairie import C_Librairie


if __name__ == '__main__':
    librairie = C_Librairie()
    for root, dirs, files in os.walk(r"/TestData"):
        for f in files:
            librairie.importJSON(os.path.join(root, f))
    print("test")
