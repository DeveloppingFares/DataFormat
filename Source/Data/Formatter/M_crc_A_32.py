from crccheck.crc import Crc32
from Source.Data.Interfaces.M_Formatter import C_Formatter


class C_crc_A_32(C_Formatter):
    def __init__(self):
        pass

    def __call__(self, valeur: bytearray) -> bytearray:
        return bytearray(Crc32.calc(valeur).to_bytes(4, 'big'))
