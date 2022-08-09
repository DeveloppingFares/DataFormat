import os
from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Bloc import C_Bloc
from Source.Data.Format.M_Field import C_Field


class C_Bitfield(C_Bloc, C_observable):
    def __init__(self, nom: str, description: str, dependance: list, elements: list):
        # Depuis Observable
        super().__init__()

        # Depuis Donnees
        self._nom: str = nom
        self._description: str = description
        self._dependance: list = dependance

        # Depuis Bloc
        self._elements: list = elements
        for element in elements:
            setattr(self, element.nom, element)

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
    def random(self) -> bytearray:
        return bytearray(os.urandom(self.taille))

    def update(self, **kwargs) -> None:
        raise NotImplementedError

    # ==================================================================================================================
    # Depuis Bloc
    # ==================================================================================================================
    @property
    def valeur(self) -> bytearray:
        if any(isinstance(attr, C_Field) for attr in self.__dict__.values()):
            v = int()
            for attr in self.__dict__.values():
                if isinstance(attr, C_Field):
                    v += attr.valeur << attr.offset
            return bytearray(v.to_bytes(self.taille, 'big'))
        else:
            raise AttributeError(f"Bitfield {self.nom} ne contient aucun élément")

    @valeur.setter
    def valeur(self, v: bytearray):
        if len(v) != self.taille:
            raise ValueError
        if any(isinstance(attr, C_Field) for attr in self.__dict__.values()):
            for attr in self.__dict__.values():
                if isinstance(attr, C_Field):
                    attr.valeur = (int.from_bytes(v, 'big') & attr.masque) >> attr.offset
        else:
            raise AttributeError(f"Bitfield {self.nom} ne contient aucun élément")

    @property
    def taille(self) -> int:
        if any(isinstance(attr, C_Field) for attr in self.__dict__.values()):
            t = int()
            for attr in self.__dict__.values():
                if isinstance(attr, C_Field):
                    t += attr.taille
        else:
            raise AttributeError(f"Bitfield {self.nom} ne contient aucun élément")
        if t % 8 != 0:
            raise AttributeError(f"Bitfield de taille {t} non aligné sur des octets")
        if t // 8 > 4:
            raise AttributeError(f"Bitfield de taille {t} supérieur à 4 octets")
        return t // 8
