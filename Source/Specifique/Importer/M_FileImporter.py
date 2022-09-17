from pathlib import Path
from Source.Commun.Data.Utilitaires.M_Constantes import E_Extension
from Source.Commun.Data.Interfaces.M_Importer import C_Importer, C_ResultatImport
from Source.Specifique.Importer.M_JsonImporter import C_JsonImporter


class C_FileImporter(C_Importer):
    def __init__(self, filepath: str):
        self.path = Path(filepath)
        self.extension = E_Extension.from_str(self.path.suffix)

    def import_file(self) -> C_ResultatImport:
        return self.get_importer().import_file()

    def get_importer(self) -> C_Importer:
        if self.extension is E_Extension.JSON:
            return C_JsonImporter(self.path)
        else:
            raise NotImplementedError
