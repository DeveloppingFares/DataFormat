import os
from Source.Observer.M_observable import C_observable
from Source.Data.Interfaces.M_Bloc import C_Bloc
from Source.Data.Format import ErreurNomAttributUtilise, ErreurAucunAttribut
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
            if not hasattr(self, element.nom):
                setattr(self, element.nom, element)
            else:
                raise ErreurNomAttributUtilise(type_element=self.__class__.__name__, nom_element=self.nom, nom_attribut=element.nom)

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

    def factory(self):
        nouvelle_instance = C_Bitfield(nom=self._nom,
                                       description=self._description,
                                       dependance=list(map(lambda x: x.factory(), self._dependance)),
                                       elements=list(map(lambda x: x.factory(), self._elements)))
        nouvelle_instance.ajout_observer()
        return nouvelle_instance

    # ==================================================================================================================
    # Depuis Observer
    # ==================================================================================================================
    def ajout_observer(self):
        for dependance in self.dependance:
            dependance.ajout_observer(self)
        for attr in self.__dict__.values():
            if isinstance(attr, C_Field):
                attr.ajout_observer()

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
            raise ErreurAucunAttribut(type_element=self.__class__.__name__, nom_element=self.nom)

    @valeur.setter
    def valeur(self, v: bytearray):
        if len(v) != self.taille:
            raise ValueError
        if any(isinstance(attr, C_Field) for attr in self.__dict__.values()):
            for attr in self.__dict__.values():
                if isinstance(attr, C_Field):
                    attr.valeur = (int.from_bytes(v, 'big') & attr.masque) >> attr.offset
        else:
            raise ErreurAucunAttribut(type_element=self.__class__.__name__, nom_element=self.nom)
        self.notify()

    @property
    def taille(self) -> int:
        if any(isinstance(attr, C_Field) for attr in self.__dict__.values()):
            t = int()
            for attr in self.__dict__.values():
                if isinstance(attr, C_Field):
                    t += attr.taille
        else:
            raise ErreurAucunAttribut(type_element=self.__class__.__name__, nom_element=self.nom)
        if t % 8 != 0:
            raise AttributeError(f"Bitfield de taille {t} non aligné sur des octets")
        if t // 8 > 4:
            raise AttributeError(f"Bitfield de taille {t} supérieur à 4 octets")
        return t // 8
