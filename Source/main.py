from datetime import datetime
from Source.Data.M_Librairie import C_Librairie


if __name__ == '__main__':
    librairie = C_Librairie()
    start = datetime.now()
    librairie.importDirectory(r"D:\Documents\Programmation\DataFormat\TestData\Format")
    end = datetime.now()
    print(str(librairie.exemple))
    print(f"Modification exemple.contenu.contenu1")
    librairie.exemple.contenu.contenu1.randomize()
    print(f"Modification exemple.contenu.contenu2")
    librairie.exemple.contenu.contenu2.randomize()
    print(f"Modification exemple.contenu.contenu3")
    librairie.exemple.contenu.contenu3.randomize()
    print(f"Modification exemple.contenu.contenu4")
    librairie.exemple.contenu.contenu4.randomize()
    print(str(librairie.exemple))
    print(str(librairie.champ_externe))
    print(f"Temps de traitement: {str(end-start)}")
