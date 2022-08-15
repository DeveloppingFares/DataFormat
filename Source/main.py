from datetime import datetime
from Source.Data.M_Librairie import C_Librairie


if __name__ == '__main__':
    librairie = C_Librairie()
    start = datetime.now()
    librairie.importDirectory(r"C:\Users\tarik\PycharmProjects\DataFormat\TestData")
    librairie.ajout_observer()
    end = datetime.now()
    print(f"Valeur Exemple: {librairie.exemple.valeur}")
    print(f"Modification exemple.contenu.contenu1")
    librairie.exemple.contenu.contenu1.valeur = librairie.exemple.contenu.contenu1.random
    print(f"Modification exemple.contenu.contenu2")
    librairie.exemple.contenu.contenu2.valeur = librairie.exemple.contenu.contenu2.random
    print(f"Valeur Exemple apres update: {librairie.exemple.valeur}")
    print(f"Valeur Champ externe apres update: {librairie.champ_externe.valeur}")
    print(f"Temps de traitement: {str(end-start)}")
