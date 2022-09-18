from abc import ABCMeta
from Source.Commun.Data.Interfaces.M_Donnees import C_Donnees
from Source.Commun.Data.Interfaces.M_Formatter import C_Formatter
from Source.Commun.Data.Utilitaires.M_Constantes import E_Format
from Source.Commun.Data.Factories.M_AbstractFactory import C_AbstractFactory


class C_Librairie(metaclass=ABCMeta):
    @classmethod
    def instancie(cls, librairie, template: C_Donnees) -> C_Donnees:
        instance = C_AbstractFactory[E_Format.from_str(template.type_element)](librairie, None).creerDonneesDepuisTemplate(template)
        instance.ajout_observer()
        return instance

    def get_formatter(self, nom: str):
        if not hasattr(self, nom):
            raise AttributeError
        elif isinstance(self.__getattribute__(nom), C_Formatter):
            return self.__getattribute__(nom)
        else:
            raise TypeError

    def ajout_observer(self):
        for attr in self.__dict__.values():
            if issubclass(type(attr), C_Donnees):
                attr.ajout_observer()
