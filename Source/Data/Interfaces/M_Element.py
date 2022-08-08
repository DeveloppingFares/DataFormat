from abc import abstractmethod
from Source.Data.Interfaces.M_Donnees import C_Donnees


class C_Element(metaclass=C_Donnees):
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
        if any("taille" in b.__dict__ for b in c.__mro__) and \
           any("valeur" in vars(b) for b in c.__mro__):
            return True
        return NotImplemented
