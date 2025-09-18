# Constante que representa a aceleração da gravidade na Terra (m/s²)
GRAVIDADE = 9.81

# Função para calcular a velocidade inicial de um objeto em queda livre
# a partir de uma determinada altura.
def calcular_velocidade_inicial(altura):
    # Fórmula: v = sqrt(2 * g * h)
    return (2 * GRAVIDADE * altura) ** 0.5
