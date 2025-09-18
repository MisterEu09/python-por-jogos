def validar_save(save):
    chaves_obrigatorias = {"nome", "nivel", "vida"}
    faltantes = chaves_obrigatorias - set(save.keys())
    
    if faltantes:
        raise KeyError(f"Chaves faltantes: {faltantes}")
    
    # Valores padrão para dados corrompidos
    save["vida"] = max(0, save.get("vida", 100))
    return save
