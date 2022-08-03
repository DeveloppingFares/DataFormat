from Source.Data.Interfaces.M_abstract_donnees import C_abstract_donnees
from Source.Format.Interfaces.M_abstract_format import C_abstract_format
from Source.Data.M_field import C_field


class C_bitfield(C_abstract_donnees):
    def __init__(self):
        self._nom: str = str()
        self._valeur: int = int()
        self._taille: int = int()  # Taille en bits

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def valeur(self) -> bytearray:
        if any(isinstance(attr, C_field) for attr in self.__dict__.values()):
            self._valeur = int()
            for attr in self.__dict__.values():
                if isinstance(attr, C_field):
                    self._valeur += attr.valeur << attr.offset
        return bytearray(self._valeur.to_bytes(self.taille, 'big'))

    @valeur.setter
    def valeur(self, v: bytearray):
        if len(v) != self.taille:
            raise ValueError
        if any(isinstance(attr, C_field) for attr in self.__dict__.values()):
            for attr in self.__dict__.values():
                if isinstance(attr, C_field):
                    attr.valeur = (int.from_bytes(v, 'big') & attr.masque) >> attr.offset
        else:
            self._valeur = int.from_bytes(v, 'big')

    @property
    def taille(self) -> int:
        if self._taille % 8 != 0 or self._taille // 8 > 4:
            raise AttributeError
        return self._taille // 8

    def importJSON(self, data: dict):
        raise NotImplementedError

    def exportJSON(self, data: dict):
        raise NotImplementedError

    def importBIN(self):
        raise NotImplementedError

    def exportBIN(self):
        raise NotImplementedError

    def add_donnees(self, donnee: C_field):
        if hasattr(self, donnee.nom):
            raise ValueError
        self._taille += donnee.taille
        setattr(self, donnee.nom, donnee)

    def add_formattage(self, formattage: C_abstract_format):
        pass
