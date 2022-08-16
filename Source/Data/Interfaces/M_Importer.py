from abc import ABCMeta, abstractmethod
from Source.Data.Importer.M_ResultatImport import C_ResultatImport


class C_Importer(metaclass=ABCMeta):
    @abstractmethod
    def import_file(self) -> C_ResultatImport:
        raise NotImplementedError
