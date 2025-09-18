
import os
import tempfile
import pytest #Se não reconhecer, instale com: pip install pytest
from salvamento_jogo import salvar_jogo, carregar_jogo


def test_salvamento_valido():
    """Testa salvamento com dados válidos"""
    dados_validos = {
        "nome": "Teste",
        "nivel": 1,
        "vida": 100,
        "inventario": ["espada", "escudo"]
    }
    
    # Usar arquivo temporário para teste
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
        temp_path = tmp.name
    
    # Substituir temporariamente o caminho do save
    original_salvar = salvar_jogo
    def salvar_temp(dados):
        return original_salvar(dados, temp_path)
    # Testar salvamento
    assert salvar_temp(dados_validos) == True

    assert os.path.exists(temp_path)
    
    # Limpar
    os.unlink(temp_path)


def test_salvamento_invalido():
    """Testa salvamento com dados inválidos"""
    dados_invalidos = {
        "nome": "Teste",
        "nivel": 1,
        "vida": 100,
        "inventario": ["espada", "escudo"],
        "funcao": lambda x: x  # Objeto não serializável
    }
    
    assert salvar_jogo(dados_invalidos) == False


def test_carregamento_inexistente():
    """Testa carregamento de arquivo inexistente"""
    assert carregar_jogo("arquivo_inexistente.json") is None


def test_carregamento_corrompido():
    """Testa carregamento de arquivo corrompido"""
    # Criar arquivo corrompido
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
        tmp.write("{isso não é json válido}")
        temp_path = tmp.name
    
    # Testar carregamento
    resultado = carregar_jogo(temp_path)
    assert resultado is None
    
    # Verificar se foi criado backup
    backups = [f for f in os.listdir('.') if f.startswith('savegame_corrupto')]
    assert len(backups) > 0
    # Limpar
    os.unlink(temp_path)
    for backup in backups:
        os.unlink(backup)



if __name__ == "__main__":
    # Executar testes
    test_salvamento_valido()
    print("✅ Teste de salvamento válido passou!")
    
    test_salvamento_invalido()
    print("✅ Teste de salvamento inválido passou!")
    
    test_carregamento_inexistente()
    print("✅ Teste de carregamento inexistente passou!")
    
    test_carregamento_corrompido()
    print("✅ Teste de carregamento corrompido passou!")
    
    print("🎉 Todos os testes passaram!")
