# Função para calcular o dano causado em um ataque
def calcular_dano(ataque, defesa):
    # O dano é o ataque menos 30% da defesa, mas nunca menor que 1
    return max(1, ataque - (defesa * 0.3))

# Função para verificar se o personagem consegue esquivar
def esquiva(agilidade):
    # Retorna True se a agilidade for maior que 7, caso contrário False
    return agilidade > 7
