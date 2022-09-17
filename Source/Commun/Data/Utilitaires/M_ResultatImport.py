from Source.Commun.Data.Utilitaires.M_Constantes import E_Format


class C_ResultatImport(object):
    def __init__(self, nom: str, format_element: str, contenu: dict):
        self.nom = nom
        self.format = E_Format.from_str(format_element)
        self.contenu = contenu
