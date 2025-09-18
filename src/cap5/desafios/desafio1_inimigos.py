inimigos = [
    {"nome": "Orc", "vida": 50, "dano": 10},
    {"nome": "Goblin", "vida": 30, "dano": 5}
]
# Adicionar
inimigos.append({"nome": "Dragão", "vida": 200, "dano": 25})


# Calcular poder
poder_total = sum(inimigo["dano"] for inimigo in inimigos)
print("Poder do grupo:", poder_total)
