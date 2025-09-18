hp_inimigo = 100
print("Inimigo tem 100 HP!")


while hp_inimigo > 0:
    dano = int(input("Dano do ataque: "))
    hp_inimigo -= dano
    print(f"HP restante: {max(0, hp_inimigo)}")


print("Inimigo derrotado!")
# Exemplo de entrada:
# Dano do ataque: 30
# Dano do ataque: 50
# Dano do ataque: 25