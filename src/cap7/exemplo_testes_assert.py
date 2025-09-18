def calcular_dano(ataque, defesa):
    return max(1, ataque - (defesa * 0.3))


def testar_calculo_dano():
    """Testa a função calcular_dano"""
    resultado = calcular_dano(50, 20)
    assert resultado == 44.0, f"Esperado 44.0, obtido {resultado}"
    print("✅ Teste passou!")


# Execute o teste
if __name__ == "__main__":
    testar_calculo_dano()
# Saída esperada: ✅ Teste passou!