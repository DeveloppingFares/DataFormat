import os
from Source.Data.M_Librairie import C_Librairie


if __name__ == '__main__':
    librairie = C_Librairie()
    librairie.importDirectory(r"C:\Users\tarik\PycharmProjects\DataFormat\TestData")
    print("test")
