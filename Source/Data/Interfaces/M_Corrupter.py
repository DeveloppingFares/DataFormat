from abc import ABCMeta, abstractmethod


class C_Corrupter(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def corrupt(cls, valeur, **kwargs):
        raise NotImplementedError

    @staticmethod
    def get_bit(valeur: int, bit_index: int) -> int:
        return valeur & (1 << bit_index)

    @staticmethod
    def set_bit(valeur: int, bit_index: int) -> int:
        return valeur | (1 << bit_index)

    @staticmethod
    def unset_bit(valeur: int, bit_index: int) -> int:
        return valeur & ~(1 << bit_index)
