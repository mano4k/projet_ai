def allowed_file(filename: str) -> bool:
    # True si l’extension est supportée. (Petite vérification sur le coté au cas oèu)
    return Path(filename).suffix.lower() in ALLOWED_EXT