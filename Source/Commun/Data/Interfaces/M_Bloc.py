from abc import ABCMeta, abstractmethod
from Source.Commun.Data.Interfaces.M_Donnees import C_Donnees
from Source.Commun.Data.Corrupter.M_AbstractCorrupter import C_AbstractCorrupter
from Source.Commun.Data.Utilitaires.M_Constantes import E_Corruption


class C_Bloc(C_Donnees, metaclass=ABCMeta):
    @property
    @abstractmethod
    def taille(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def valeur(self) -> bytearray:
        raise NotImplementedError

    @valeur.setter
    @abstractmethod
    def valeur(self, v: bytearray):
        raise NotImplementedError

    # ==================================================================================================================
    # Depuis Donnees
    # ==================================================================================================================
    @property
    @abstractmethod
    def nom(self) -> str:
        raise NotImplementedError

    @nom.setter
    @abstractmethod
    def nom(self, v: str):
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError

    @description.setter
    @abstractmethod
    def description(self, v: str):
        raise NotImplementedError

    @property
    @abstractmethod
    def random(self):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, c):
        if issubclass(c, C_Donnees) and "elements" in c.__dict__ and "taille" in vars(c) and "valeur" in vars(c):
            return True
        return False

    def _corrupt(self, type_corruption: str, **kwargs) -> bytearray:
        return C_AbstractCorrupter[E_Corruption.from_str(type_corruption)].corrupt(self.valeur, **kwargs)

    def randomize(self):
        self.valeur = self.random

    def __str__(self):
        desc = str()
        desc += f"{self.nom}: {self.valeur.hex()}\n"
        desc += f"\tType: {str(type(self))}\n"
        desc += f"\tDescription: {self.description}\n"
        desc += f"\tTaille: {str(self.taille)} octets\n"
        for nom_attr, val_attr in self.__dict__.items():
            if issubclass(type(val_attr), C_Donnees):
                desc += f"{str(val_attr)}"
        return desc
