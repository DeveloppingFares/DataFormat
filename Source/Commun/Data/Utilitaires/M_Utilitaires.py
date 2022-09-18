def extrait_attribut(nom_attribut: str, type_attribut, contenu: dict, obligatoire: bool = True):
    attr = contenu.get(nom_attribut)
    if attr is None:
        if obligatoire:
            raise KeyError(f"L'attribut {nom_attribut} est introuvable")
        else:
            return None
    if not isinstance(attr, type_attribut):
        raise TypeError(f"L'attribut {nom_attribut} est de type {str(type(attr))}. Attendu: {str(type_attribut)}")
    return attr


def cherche_attribut(objet, chemin_attribut: list):
    for attr in chemin_attribut:
        if attr in objet.__dict__:
            objet = objet.__getattribute__(attr)
        else:
            raise KeyError(f"L'attribut {'.'.join(chemin_attribut)} est introuvable")
    return objet
