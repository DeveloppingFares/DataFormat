from Source.Specifique.M_LibrairieExemple import C_LibrairieExemple
import cProfile
import pstats


def execute():
    librairie = C_LibrairieExemple()
    librairie.importDirectory(r"D:\Documents\Programmation\DataFormat\TestData\Format")
    print(str(librairie.exemple))
    print(str(librairie.exemple.crc))
    librairie.exemple.contenu.contenu1.randomize()
    librairie.exemple.contenu.contenu2.randomize()
    librairie.exemple.contenu.contenu3.randomize()
    librairie.exemple.contenu.contenu4.randomize()
    print(str(librairie.exemple.crc))
    new_instance = librairie.instancie(librairie, librairie.exemple)
    print(str(new_instance.crc))
    new_instance.contenu.contenu1.randomize()
    print(str(librairie.exemple.crc))
    print(str(new_instance.crc))
    new_instance.contenu.contenu2.randomize()
    print(str(librairie.exemple.crc))
    print(str(new_instance.crc))

    print(librairie.exemple.valeur.hex())
    print(librairie.exemple.corrupt(element_corrompu="crc", type_corruption='bitabit', bit_index=31).hex())
    print(librairie.exemple.valeur.hex())
    print(librairie.exemple.valeur.hex())
    print(librairie.exemple.corrupt(element_corrompu="contenu4", type_corruption='bitabit', bit_index=31).hex())
    print(librairie.exemple.valeur.hex())
    print(librairie.bitfield1.valeur.hex())
    print(librairie.bitfield1.corrupt(element_corrompu="champ4", type_corruption='bitabit', bit_index=7).hex())
    print(librairie.bitfield1.valeur.hex())

    print(new_instance.valeur.hex())
    print(new_instance.corrupt(element_corrompu="crc", type_corruption='bitabit', bit_index=31).hex())
    print(new_instance.valeur.hex())
    print(new_instance.valeur.hex())
    print(new_instance.corrupt(element_corrompu="contenu", type_corruption='bitabit', bit_index=31).hex())
    print(new_instance.valeur.hex())
    print(new_instance.contenu.valeur.hex())
    print(new_instance.contenu.corrupt(element_corrompu="champ4", type_corruption='bitabit', bit_index=7).hex())
    print(new_instance.contenu.valeur.hex())


if __name__ == '__main__':
    cProfile.run("execute()", 'datastats')
    p = pstats.Stats('datastats')
    p.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats()
    # execute()
