import fisica

def test_calcular_velocidade_inicial():
    # Teste com altura conhecida
    resultado = fisica.calcular_velocidade_inicial(10)
    esperado = 14.01
    assert abs(resultado - esperado) < 0.1, f"Esperado {esperado}, obtido {resultado}"
    print("✅ Teste passou!")


if __name__ == "__main__":
    test_calcular_velocidade_inicial()
