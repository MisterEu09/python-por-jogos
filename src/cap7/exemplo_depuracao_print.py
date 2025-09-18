def calcular_dano(ataque, defesa):
    print(f"DEBUG: ataque={ataque}, defesa={defesa}")  # Depuração
    return max(1, ataque - (defesa * 0.3))


dano = calcular_dano(50, 20)
print(f"Dano calculado: {dano}")
