from Source.Data.Interfaces.M_Donnees import C_Donnees


class C_Field(C_Donnees):
    def __init__(self, nom: str, description: str, dependance: list, taille: int, offset: int, valeur: int):
        super().__init__()
        self._valeur: int = valeur
        self._offset: int = offset
        self._taille: int = taille
        self._masque: int = (0xFFFFFFFF >> (32 - self._taille)) << self._offset

        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

    @property
    def valeur(self) -> int:
        return self._valeur

    @valeur.setter
    def valeur(self, v: int):
        self._valeur = v

    @property
    def offset(self) -> int:
        return self._offset

    @property
    def masque(self) -> int:
        return self._masque

    @property
    def taille(self) -> int:
        return self._taille

    # ==================================================================================================================
    # Depuis Donnees
    # ==================================================================================================================
    @property
    def nom(self) -> str:
        return self._nom

    @property
    def description(self) -> str:
        return self._description

    @property
    def dependance(self) -> list:
        return self._dependance

    @property
    def random(self) -> int:
        raise NotImplementedError
