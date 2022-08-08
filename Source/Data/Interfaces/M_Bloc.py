from abc import abstractmethod
from Source.Data.Interfaces.M_Donnees import C_Donnees


class C_Bloc(metaclass=C_Donnees):
    @property
    @abstractmethod
    def taille(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def valeur(self) -> str:
        raise NotImplementedError

    @valeur.setter
    @abstractmethod
    def valeur(self, v: str):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, c):
        if any("elements" in b.__dict__ for b in c.__mro__) and \
           any("taille" in vars(b) for b in c.__mro__) and \
           any("valeur" in vars(b) for b in c.__mro__):
            return True
        return NotImplemented
