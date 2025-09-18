# Função responsável por verificar se o jogador pode subir de nível
def subir_nivel(nivel_atual, xp_ganho):
    # Calcula o XP necessário para subir de nível (100 vezes o nível atual)
    xp_necessario = nivel_atual * 100
    # Se o XP ganho for suficiente para subir de nível
    if xp_ganho >= xp_necessario:
        novo_nivel = nivel_atual + 1  # Incrementa o nível
        xp_restante = xp_ganho - xp_necessario  # Calcula o XP que sobra após subir de nível
        print("🎉 NOVO NÍVEL! 🎉")  # Mensagem de parabéns
        return novo_nivel, xp_restante  # Retorna o novo nível e o XP restante
    # Se não for suficiente, retorna o nível atual e o XP atual
    return nivel_atual, xp_ganho

# Função principal do programa
def main():
    nivel = 1  # Nível inicial do jogador
    xp = 0     # XP inicial do jogador
    print("Bem-vindo ao sistema de níveis!")
    print("Ganhe XP para subir de nível. Digite 'sair' para encerrar.\n")

    # Loop principal do jogo
    while True:
        # Mostra o status atual do jogador
        print(f"Nível atual: {nivel}, XP atual: {xp}, XP para próximo nível: {nivel * 100 - xp}")
        entrada = input("Quanto XP você ganhou? ")  # Solicita ao usuário o XP ganho
        if entrada.lower() == 'sair':  # Permite sair do programa
            print("Até a próxima!")
            break
        try:
            xp_ganho = int(entrada)  # Tenta converter a entrada para inteiro
            if xp_ganho < 0:
                print("XP não pode ser negativo.")  # Validação para XP negativo
                continue
            xp += xp_ganho  # Adiciona o XP ganho ao XP atual
            # Verifica se é possível subir de nível (pode subir múltiplos níveis de uma vez)
            while True:
                novo_nivel, xp = subir_nivel(nivel, xp)
                if novo_nivel == nivel:  # Se não subiu de nível, sai do loop
                    break
                nivel = novo_nivel  # Atualiza o nível
                print(f"Nível atual: {nivel}, XP restante: {xp}")  # Mostra novo status após subir de nível
        except ValueError:
            print("Por favor, digite um número válido ou 'sair'.")  # Mensagem de erro para entrada inválida

# Executa a função principal se o arquivo for executado diretamente
if __name__ == "__main__":
    main()
