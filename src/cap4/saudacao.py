def saudar_jogador(nome):
    """Exibe mensagem de boas-vindas personalizada"""
    print(f"Bem-vindo(a), {nome}! Prepare-se para a aventura!")
    return len(nome)  # Retorna o tamanho do nome



# Chamando a função
tamanho_nome = saudar_jogador("Arya")
print(f"Seu nome tem {tamanho_nome} letras!")
