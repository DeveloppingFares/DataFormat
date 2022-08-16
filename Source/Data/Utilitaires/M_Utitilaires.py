def extrait_attribut(nom_attribut: str, type_attribut, contenu: dict):
    attr = contenu.get(nom_attribut)
    if attr is None:
        raise KeyError(f"L'attribut {nom_attribut} est introuvable")
    if not isinstance(attr, type_attribut):
        raise TypeError(f"L'attribut {nom_attribut} est de type {str(type(attr))}. Attendu: {str(type_attribut)}")
    return attr
