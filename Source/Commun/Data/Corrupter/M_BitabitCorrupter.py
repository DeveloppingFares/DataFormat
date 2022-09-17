from typing import Union
from Source.Commun.Data.Interfaces.M_Corrupter import C_Corrupter
from Source.Commun.Data.Utilitaires.M_Utilitaires import extrait_attribut


class C_BitabitCorrupter(C_Corrupter):
    @classmethod
    def corrupt(cls, valeur: Union[int, bytearray], **kwargs) -> Union[int, bytearray]:
        bit_index = extrait_attribut(nom_attribut="bit_index", type_attribut=int, contenu=kwargs)
        if bit_index is None:
            raise ValueError

        if isinstance(valeur, bytearray):
            byte_index = len(valeur) - (bit_index // 8) - 1
            corrupted_int = valeur[byte_index]
            corruption = valeur[:]
            corruption[byte_index:byte_index+1] = bytearray([cls.unset_bit(corrupted_int, bit_index % 8) if cls.get_bit(corrupted_int, bit_index % 8) else cls.set_bit(corrupted_int, bit_index % 8)])
            return corruption
        elif isinstance(valeur, int):
            corruption = valeur
            return cls.unset_bit(corruption, bit_index) if cls.get_bit(corruption, bit_index) else cls.set_bit(corruption, bit_index)
        else:
            raise NotImplementedError
