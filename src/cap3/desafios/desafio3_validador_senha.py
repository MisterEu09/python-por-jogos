# Loop infinito para solicitar a senha até que seja válida
while True:
    # Solicita ao usuário que crie uma senha
    senha = input("Crie uma senha (min. 8 chars com número): ")
    # Verifica se a senha tem menos de 8 caracteres
    if len(senha) < 8:
        print("Senha muito curta! Min. 8 caracteres.")
    # Verifica se a senha não contém nenhum número
    elif not any(char.isdigit() for char in senha):
        print("Adicione pelo menos um número!")
    # Se a senha atende aos requisitos, informa que é válida e encerra o loop
    else:
        print("Senha válida!")
        break

# Exemplo de entrada:
# Crie uma senha (min. 8 chars com número): senha123
# Saída esperada: Senha válida!
