from abc import ABCMeta, abstractmethod


class C_abstract_format(metaclass=ABCMeta):
    @property
    @abstractmethod
    def valeur(self) -> bytearray:
        raise NotImplementedError

    @valeur.setter
    @abstractmethod
    def valeur(self, v: bytearray):
        raise NotImplementedError

    @abstractmethod
    def importJSON(self, filepath: str):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, c):
        if any("valeur" in vars(b) for b in c.__mro__) and \
           any("importJSON" in b.__dict__ for b in c.__mro__):
            return True
        return NotImplemented