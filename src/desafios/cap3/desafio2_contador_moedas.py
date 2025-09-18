total = 0
for fase in range(1, 6):
    moedas = int(input(f"Moedas na fase {fase}: "))
    total += moedas


print(f"Total: {total} moedas")
if total >= 100:
    print("Baú dourado desbloqueado!")
else:
    print("Baú dourado bloqueado!")
# Exemplo de entrada:
# Moedas na fase 1: 20
# Moedas na fase 2: 15
# Moedas na fase 3: 30