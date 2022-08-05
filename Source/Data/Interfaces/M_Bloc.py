from abc import abstractmethod
from Source.Data.Interfaces.M_Donnees import C_Donnees


class C_Bloc(C_Donnees):
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
        if any("valeur" in vars(b) for b in c.__mro__) and \
           any("taille" in vars(b) for b in c.__mro__):
            return True
        return NotImplemented
