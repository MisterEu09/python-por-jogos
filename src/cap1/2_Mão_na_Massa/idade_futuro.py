# Passo 1: Capturar dados
nome = input("Seu nome: ")
idade_atual = input("Sua idade atual: ")

# Passo 2: Converter texto para número
idade_numero = int(idade_atual)

# Passo 3: Calcular idade futura
idade_futura = idade_numero + 10

# Passo 4: Exibir resultado formatado
print(f"{nome}, daqui a 10 anos você terá {idade_futura} anos!")
