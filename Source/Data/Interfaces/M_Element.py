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

    def randomize(self):
        self.valeur = self.random

    def __str__(self):
        return f"""{self.nom}: {self.valeur.hex()}
\tType: {str(type(self))}
\tDescription: {self.description}
\tTaille: {str(self.taille)} octets
"""
