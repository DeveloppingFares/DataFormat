from abc import ABCMeta, abstractmethod
from Source.Observer.M_observer import C_observer


class C_Donnees(C_observer, metaclass=ABCMeta):
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
    def dependance(self) -> list:
        raise NotImplementedError

    @dependance.setter
    @abstractmethod
    def dependance(self, v: list):
        raise NotImplementedError

    @property
    @abstractmethod
    def random(self) -> int | bytearray:
        raise NotImplementedError

    @abstractmethod
    def ajout_observer(self, observer: C_observer):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, c):
        if "nom" in vars(c) and "description" in vars(c) and "dependance" in c.__dict__ and "ajout_observer" in vars(c):
            return True
        return False
