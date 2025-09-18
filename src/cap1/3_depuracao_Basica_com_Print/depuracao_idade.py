# Programa com depuração
nome = input("Seu nome: ")
print(f"DEBUG: nome = {nome}")


idade_atual = input("Sua idade atual: ")
print(f"DEBUG: idade_atual = {idade_atual} (tipo: {type(idade_atual)})")


# Tenta converter para inteiro
try:
    idade_numero = int(idade_atual)
    print(f"DEBUG: idade_numero = {idade_numero} (tipo: {type(idade_numero)})")
except ValueError:
    print("DEBUG: Não foi possível converter para inteiro!")


idade_futura = idade_numero + 10
print(f"{nome}, daqui a 10 anos você terá {idade_futura} anos!")
