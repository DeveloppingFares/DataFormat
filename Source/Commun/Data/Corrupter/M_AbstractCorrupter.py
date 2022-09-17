from Source.Commun.Data.Utilitaires.M_Constantes import E_Corruption
from Source.Commun.Data.Corrupter.M_BitabitCorrupter import C_BitabitCorrupter


class C_AbstractCorrupter:
    def __class_getitem__(cls, type_corruption: E_Corruption) -> type:
        if type_corruption == E_Corruption.bitabit:
            return C_BitabitCorrupter
        else:
            raise NotImplementedError

    def corrupt(self):
        raise NotImplementedError
