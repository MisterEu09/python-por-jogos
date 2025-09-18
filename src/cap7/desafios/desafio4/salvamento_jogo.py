# salvamento_jogo.py
import json
import os
import shutil

def salvar_jogo(dados, caminho='src/cap7/desafios/desafio4/savegame.json'):
    try:
        with open(caminho, 'w') as f:
            json.dump(dados, f)
        return True
    except Exception:
        return False

def carregar_jogo(caminho='src/cap7/desafios/desafio4/savegame.json'):
    try:
        with open(caminho, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        # Criar backup do arquivo corrompido
        backup_nome = f"savegame_corrupto_{os.path.basename(caminho)}"
        shutil.copy(caminho, backup_nome)
        return None