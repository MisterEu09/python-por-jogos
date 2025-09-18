# Função que retorna um único valor
def calcular_dano(ataque, defesa):
    """Calcula dano com base na defesa"""
    # O dano é o ataque menos 30% da defesa, mas nunca menor que 1
    return max(1, ataque - (defesa * 0.3))

# Função que retorna múltiplos valores
def calcular_posicao(x, y, velocidade):
    """Calcula nova posição baseada na velocidade"""
    # Calcula o novo valor de x somando a velocidade no eixo x
    novo_x = x + velocidade[0]
    # Calcula o novo valor de y somando a velocidade no eixo y
    novo_y = y + velocidade[1]
    # Retorna os novos valores como uma tupla
    return novo_x, novo_y  # Tupla implícita

# Exemplo de uso das funções
dano = calcular_dano(50, 20)
print(f"Dano causado: {dano}")  # Dano causado: 44.0

pos_x, pos_y = calcular_posicao(100, 200, (3, -1))
print(f"Nova posição: ({pos_x}, {pos_y})")  # Nova posição: (103, 199)
