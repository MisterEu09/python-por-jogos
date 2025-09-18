regioes = {
    "floresta": {"cogumelo", "flor", "fruta"},
    "montanha": {"cristal", "minério", "fóssil"}
}


colecao_jogador = set()


# Verificar coleção completa
def colecao_completa(regiao):
    return regioes[regiao].issubset(colecao_jogador)
print (regioes)
