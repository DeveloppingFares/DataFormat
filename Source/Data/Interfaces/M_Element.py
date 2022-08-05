from abc import ABCMeta, abstractmethod
from Source.Data.Interfaces.M_Donnees import C_Donnees


class C_Bloc(metaclass=C_Donnees):
    @property
    @abstractmethod
    def valeur(self) -> bytearray:
        raise NotImplementedError

    @valeur.setter
    @abstractmethod
    def valeur(self, v: bytearray):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, c):
        if any("taille" in b.__dict__ for b in c.__mro__) and \
           any("valeur" in vars(b) for b in c.__mro__):
            return True
        return NotImplemented