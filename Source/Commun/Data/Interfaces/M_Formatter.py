from abc import ABCMeta, abstractmethod


class C_Formatter(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, valeur: bytearray) -> bytearray:
        raise NotImplementedError
