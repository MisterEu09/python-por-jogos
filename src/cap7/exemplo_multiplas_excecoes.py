inventario = ["Espada", "Escudo", "Poção"]
try:
    indice = int(input("Índice do item: "))
    print(inventario[indice])
except ValueError:
    print("Índice deve ser número!")
except IndexError:
    print("Índice fora do alcance!")
