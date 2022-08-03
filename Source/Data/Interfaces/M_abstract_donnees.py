from abc import ABCMeta, abstractmethod


class C_abstract_donnees(metaclass=ABCMeta):
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

    @abstractmethod
    def importJSON(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def exportJSON(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def importBIN(self):
        raise NotImplementedError

    @abstractmethod
    def exportBIN(self):
        raise NotImplementedError

    @abstractmethod
    def add_donnees(self, donnees):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, c):
        if any("nom" in vars(b) for b in c.__mro__) and \
           any("valeur" in vars(b) for b in c.__mro__) and \
           any("taille" in vars(b) for b in c.__mro__) and \
           any("importJSON" in b.__dict__ for b in c.__mro__) and \
           any("exportJSON" in b.__dict__ for b in c.__mro__) and \
           any("importBIN" in b.__dict__ for b in c.__mro__) and \
           any("exportBIN" in b.__dict__ for b in c.__mro__) and \
           any("add_donnees" in b.__dict__ for b in c.__mro__):
            return True
        return NotImplemented
