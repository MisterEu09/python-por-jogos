# Recebe texto do usuário
idade_texto = input("Quantos anos você tem? ")
print(f"DEBUG: idade_texto = '{idade_texto}', tipo = {type(idade_texto)}")
# Tenta converter para inteiro
try:
    idade = int(idade_texto)
    print(f"DEBUG: idade = {idade}, tipo = {type(idade)}")
except ValueError:
    print("DEBUG: Não foi possível converter para inteiro!")
    # Define um valor padrão para evitar erros
    idade = 0
    print(f"DEBUG: idade definida para valor padrão: {idade}")

# Só calcula se a conversão foi bem-sucedida
if idade_texto.isdigit():
    idade_em_2030 = idade + (2030 - 2024)
    print(f"Em 2030, você terá {idade_em_2030} anos!")
else:
    print("Não foi possível calcular sua idade em 2030 devido à entrada inválida.")