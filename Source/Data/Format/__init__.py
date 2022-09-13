class ErreurNomAttributUtilise(Exception):
    def __init__(self, type_element: str, nom_element: str, nom_attribut: str):
        super().__init__(f"L'element {nom_element} de type {type_element} contient deja un attribut {nom_attribut}")


class ErreurAucunAttribut(Exception):
    def __init__(self, type_element: str, nom_element: str):
        super().__init__(f"L'element {nom_element} de type {type_element} ne contient aucun attribut")


class ErreurValeurHorsLimite(Exception):
    def __init__(self, nom_attribut: str, taille_attendue: int, taille_fournie: int):
        super().__init__(f"La taille de la valeur fournie ({taille_fournie}) pour l'attribut {nom_attribut} est differente de celle attendue ({taille_attendue}).")
