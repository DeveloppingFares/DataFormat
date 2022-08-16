from abc import ABCMeta, abstractmethod
from Source.Data.Interfaces.M_Donnees import C_Donnees


class C_Bloc(C_Donnees, metaclass=ABCMeta):
    @property
    @abstractmethod
    def taille(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def valeur(self) -> bytearray:
        raise NotImplementedError

    @valeur.setter
    @abstractmethod
    def valeur(self, v: bytearray):
        raise NotImplementedError

    # ==================================================================================================================
    # Depuis Donnees
    # ==================================================================================================================
    @property
    @abstractmethod
    def nom(self) -> str:
        raise NotImplementedError

    @nom.setter
    @abstractmethod
    def nom(self, v: str):
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError

    @description.setter
    @abstractmethod
    def description(self, v: str):
        raise NotImplementedError

    @property
    @abstractmethod
    def random(self) -> int | bytearray:
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, c):
        if issubclass(c, C_Donnees) and "elements" in c.__dict__ and "taille" in vars(c) and "valeur" in vars(c):
            return True
        return False
