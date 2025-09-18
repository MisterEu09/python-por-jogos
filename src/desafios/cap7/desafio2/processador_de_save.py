from desafio2_validador_save import validar_save  # Importa a função do outro arquivo

def carregar_e_processar_save(save):
    try:
        save_validado = validar_save(save)
        print("Save validado com sucesso:", save_validado)
        return save_validado
    except KeyError as erro:
        print("Erro ao validar save:", erro)
        return None

# Exemplo de uso
if __name__ == "__main__":
    exemplo_save = {
        "nome": "Herói",
        "nivel": 5,
        # "vida" está faltando para simular dado corrompido
    }

    resultado = carregar_e_processar_save(exemplo_save)