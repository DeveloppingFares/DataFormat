from Source.Data.M_donnees import C_donnees
import json

if __name__ == '__main__':
    with open(r"D:\Documents\Programmation\DataFormat\TestData\package.json") as f:
        myData = C_donnees(nom="package")
        myData.importJSON(json.load(f))
    print("test")
