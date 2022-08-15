from abc import ABCMeta, abstractmethod
from Source.Data.Interfaces.M_Donnees import C_Donnees


class C_Element(C_Donnees, metaclass=ABCMeta):
    @property
    @abstractmethod
    def valeur(self) -> bytearray:
        raise NotImplementedError

    @valeur.setter
    @abstractmethod
    def valeur(self, v: bytearray):
        raise NotImplementedError

    @property
    @abstractmethod
    def taille(self) -> int:
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, c):
        if issubclass(c, C_Donnees) and "taille" in vars(c) and "valeur" in vars(c) and "offset" not in vars(c):
            return True
        return False
