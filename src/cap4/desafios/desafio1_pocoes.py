# Define a função que mistura dois tipos de poções
def misturar_pocoes(tipo1, tipo2):
    # Dicionário com combinações possíveis e seus resultados
    combinacoes = {
        ("fogo", "gelo"): "nuvem",
        ("agua", "terra"): "lama",
        ("luz", "sombra"): "crepusculo"
    }
    # Retorna o resultado da combinação ou uma mensagem de falha
    return combinacoes.get((tipo1, tipo2), "fusão falhou")

# Testa a função com diferentes combinações de poções
print(misturar_pocoes("fogo", "gelo"))      # Saída: nuvem
print(misturar_pocoes("agua", "terra"))     # Saída: lama
print(misturar_pocoes("luz", "sombra"))     # Saída: crepusculo
print(misturar_pocoes("fogo", "agua"))      # Saída: fusão falhou

# Exemplos de entrada:
# misturar_pocoes("fogo", "gelo") -> Saída: nuvem
# misturar_pocoes("agua", "terra") -> Saída: lama  
# misturar_pocoes("luz", "sombra") -> Saída: crepusculo
# misturar_pocoes("fogo", "agua") -> Saída: fusão falhou
