arma = "Espada Longa"   # string
dano = 15               # int
preco = 120.50          # float
disponivel = True       # bool
print(f"Arma: {arma}, Dano: {dano}, Preço: {preco}, Disponível: {disponivel}")

# Método antigo (concatenar)
print("Dano da " + arma + ": " + str(dano))

# Método moderno (f-string)
print(f"Preço: {preco:.2f} moedas")