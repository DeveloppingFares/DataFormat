from Source.Data.Interfaces.M_Bloc import C_Bloc
from Source.Data.M_Field import C_Field


class C_Bitfield(C_Bloc):
    def __init__(self, nom: str, dependance: list, elements: list):
        super().__init__()
        self._nom: str = nom
        self._valeur: int = int()
        self._taille: int = 0  # Taille en bits
        self._dependance: list = dependance
        for element in elements:
            if isinstance(element, dict):
                if element.get("type") == C_Bloc.type_donnees.field.value:
                    self.add_donnees(C_Field(**element))
                else:
                    raise ValueError
            elif isinstance(element, C_Field):
                self.add_donnees(element)
            else:
                raise ValueError

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def valeur(self) -> bytearray:
        if any(isinstance(attr, C_Field) for attr in self.__dict__.values()):
            self._valeur = int()
            for attr in self.__dict__.values():
                if isinstance(attr, C_Field):
                    self._valeur += attr.valeur << attr.offset
        return bytearray(self._valeur.to_bytes(self.taille, 'big'))

    @valeur.setter
    def valeur(self, v: bytearray):
        if len(v) != self.taille:
            raise ValueError
        if any(isinstance(attr, C_Field) for attr in self.__dict__.values()):
            for attr in self.__dict__.values():
                if isinstance(attr, C_Field):
                    attr.valeur = (int.from_bytes(v, 'big') & attr.masque) >> attr.offset
        else:
            self._valeur = int.from_bytes(v, 'big')

    @property
    def taille(self) -> int:
        if self._taille % 8 != 0 or self._taille // 8 > 4:
            raise AttributeError
        return self._taille // 8

    def add_donnees(self, donnee: C_Field):
        if hasattr(self, donnee.nom):
            raise ValueError
        self._taille += donnee.taille
        setattr(self, donnee.nom, donnee)
