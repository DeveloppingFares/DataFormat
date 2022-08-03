from abc import ABCMeta


class C_abstract_donnees(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, c):
        if any("valeur" in b.__dict__ for b in c.__mro__):
            return True