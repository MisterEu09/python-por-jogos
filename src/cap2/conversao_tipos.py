# Recebe texto do usuário
idade_texto = input("Quantos anos você tem? ")  # Ex: "25"

# Converte para inteiro
idade = int(idade_texto)

# Agora podemos calcular!
idade_em_2030 = idade + (2030 - 2024)
print(f"Em 2030, você terá {idade_em_2030} anos!")