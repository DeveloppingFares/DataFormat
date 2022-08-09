from abc import ABCMeta, abstractmethod
from Source.Observer.M_observer import C_observer
from enum import Enum


class C_Donnees(C_observer, metaclass=ABCMeta):
    class type_donnees(Enum):
        bitfield = "bitfield"
        buffer = "buffer"
        enumerate = "enumerate"
        field = "field"
        package = "package"
        processed = "processed"
        range = "range"

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
        if any("nom" in vars(b) for b in c.__mro__) and \
           any("description" in vars(b) for b in c.__mro__) and \
           any("dependance" in b.__dict__ for b in c.__mro__):
            return True
        return NotImplemented
