import fisica  # Importa o módulo de física personalizado

altura_torre = 10  # Define a altura da torre em metros

# Calcula a velocidade inicial necessária para atingir o solo a partir da altura especificada
velocidade = fisica.calcular_velocidade_inicial(altura_torre)

# Exibe a velocidade ao tocar o chão, formatada com duas casas decimais
print(f"Velocidade ao tocar o chão: {velocidade:.2f} m/s")
# Saída esperada: Velocidade ao tocar o chão: 14.01 m/s