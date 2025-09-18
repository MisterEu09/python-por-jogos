try:
    with open("src/cap7/pontuacao.txt", "r") as arquivo:
        pontos = int(arquivo.read())
except ValueError:
    print("Pontuação inválida!")
except FileNotFoundError:
    print("Arquivo não encontrado!")
else:
    print(f"Pontuação atual: {pontos}")  # Só executa se não der erro
