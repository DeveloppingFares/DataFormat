from Source.Data.Formatter.M_crc_A_32 import C_crc_A_32


class C_LibrairieFormatter(object):
    def __init__(self):
        self.crc_A_32 = C_crc_A_32()

    def get_formatter(self, nom: str):
        if not hasattr(self, nom):
            raise AttributeError
        return self.__getattribute__(nom)
