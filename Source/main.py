from datetime import datetime
from Source.Data.M_Librairie import C_Librairie


if __name__ == '__main__':
    librairie = C_Librairie()
    start = datetime.now()
    librairie.importDirectory(r"C:\Users\tarik\PycharmProjects\DataFormat\TestData")
    end = datetime.now()
    print(f"Valeur Exemple: {librairie.exemple.valeur}")
    print(f"Temps de traitement: {str(end-start)}")
