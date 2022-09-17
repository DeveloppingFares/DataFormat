from datetime import datetime
from Source.Data.M_Librairie import C_Librairie


if __name__ == '__main__':
    librairie = C_Librairie()
    start = datetime.now()
    librairie.importDirectory(r"D:\Documents\Programmation\DataFormat\TestData\Format")
    end = datetime.now()
    print(str(librairie.exemple.crc))
    librairie.exemple.contenu.contenu1.randomize()
    librairie.exemple.contenu.contenu2.randomize()
    librairie.exemple.contenu.contenu3.randomize()
    librairie.exemple.contenu.contenu4.randomize()
    print(str(librairie.exemple.crc))
    new_instance = librairie.instancie(librairie.exemple)
    print(str(new_instance.crc))
    new_instance.contenu.contenu1.randomize()
    new_instance.contenu.contenu2.randomize()
    new_instance.contenu.contenu3.randomize()
    new_instance.contenu.contenu4.randomize()
    print(str(new_instance.crc))
