class C_Field(object):
    def __init__(self, nom: str, taille: int, offset: int, valeur: int = int()):
        self._nom: str = nom
        self._valeur: int = valeur
        self._offset: int = offset
        self._taille: int = taille
        self._masque = (0xFFFFFFFF >> (32 - self._taille)) << self._offset

    @property
    def nom(self) -> str:
        return self._nom

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
