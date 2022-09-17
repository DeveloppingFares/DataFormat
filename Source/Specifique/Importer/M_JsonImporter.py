import json
from pathlib import Path
from Source.Commun.Data.Interfaces.M_Importer import C_Importer, C_ResultatImport
from Source.Commun.Data.Utilitaires.M_Utilitaires import extrait_attribut


class C_JsonImporter(C_Importer):
    def __init__(self, filepath: Path):
        if not filepath.exists():
            raise FileNotFoundError
        self.filepath = filepath

    def import_file(self) -> C_ResultatImport:
        with self.filepath.open() as fp:
            kwargs = json.load(fp)
        nom_element = extrait_attribut(nom_attribut="nom", type_attribut=str, contenu=kwargs)
        format_element = extrait_attribut(nom_attribut="type_element", type_attribut=str, contenu=kwargs)
        return C_ResultatImport(nom=nom_element, format_element=format_element, contenu=kwargs)
