from Source.Data.Interfaces.M_abstract_donnees import C_abstract_donnees
from Source.Format.Interfaces.M_abstract_format import C_abstract_format


class C_donnees(C_abstract_donnees):
    def __init__(self):
        self._nom: str = str()
        self._valeur: bytearray = bytearray()
        self._taille: int = int()

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def valeur(self) -> bytearray:
        if any(issubclass(type(attr), C_abstract_donnees) for attr in self.__dict__.values()):
            v = bytearray()
            for attr in self.__dict__.values():
                if issubclass(type(attr), C_abstract_donnees):
                    v += attr.valeur
            return v
        elif len(self._valeur) != 0:
            return self._valeur
        else:
            raise AttributeError

    @valeur.setter
    def valeur(self, v: bytearray):
        if len(v) != self._taille:
            raise ValueError
        if any(issubclass(type(attr), C_abstract_donnees) for attr in self.__dict__.values()):
            for attr in self.__dict__.values():
                if issubclass(type(attr), C_abstract_donnees):
                    attr.valeur = v[:attr.taille]
                    del v[:attr.taille]
            if len(v) != 0:
                raise Exception
        elif len(self._valeur):
            self._valeur = v
        else:
            raise ValueError

    def taille(self) -> int:
        return self._taille

    def importJSON(self, data: dict):
        raise NotImplementedError

    def exportJSON(self, data: dict):
        raise NotImplementedError

    def importBIN(self):
        raise NotImplementedError

    def exportBIN(self):
        raise NotImplementedError

    def add_donnees(self, donnee: C_abstract_donnees):
        if hasattr(self, donnee.nom):
            raise ValueError
        self._taille += donnee.taille
        setattr(self, donnee.nom, donnee)

    def add_formattage(self, formattage: C_abstract_format):
        pass
