import json
import pygame
import os

pygame.init()
pygame.mixer.init()

def salvar_jogo(dados):
    try:
        with open("src/cap7/Mini-Projeto_Sistema_de_Salvamento_Robustecido/savegame.json", "w") as f:
            json.dump(dados, f)
        print("✅ Progresso salvo com sucesso!")
        return True
    except (IOError, PermissionError) as e:
        print(f"❌ Falha ao salvar: {e}")
        return False
    except TypeError as e:
        print(f"❌ Dados inválidos: {e}")
        return False

def carregar_recursos():
    recursos = {}
    img_path = os.path.abspath("assets/cenario.png")
    audio_path = os.path.abspath("assets/trilha.wav")
    print(f"Tentando carregar imagem de: {img_path}")
    print(f"Tentando carregar áudio de: {audio_path}")
    try:
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Imagem não encontrada: {img_path}")
        recursos["fundo"] = pygame.image.load(img_path).convert()
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Áudio não encontrado: {audio_path}")
        recursos["musica"] = pygame.mixer.Sound(audio_path)
        print("✅ Recursos carregados com sucesso!")
    except (pygame.error, FileNotFoundError) as e:
        print(f"⚠️ Erro ao carregar recurso: {e}")
        recursos["fundo"] = pygame.Surface((600, 200))
        recursos["fundo"].fill((30, 30, 50))
        recursos["musica"] = None
    finally:
        return recursos

# Teste
dados_jogador = {
    "nome": "Arya",
    "nivel": 5,
    "inventario": ["espada", "escudo"]
}
if salvar_jogo(dados_jogador):
    print("Salvamento concluído!")
# --- Tela para mostrar imagem e tocar áudio ---
tela = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Visualização de Recursos")

recursos_carregados = carregar_recursos()
print("Recursos prontos:", list(recursos_carregados.keys()))

# Mostra só a imagem por 1 segundo antes de tocar a música
tela.blit(recursos_carregados["fundo"], (0, 0))
pygame.display.flip()
pygame.time.wait(1000)  # 1000 ms = 1 segundo

if recursos_carregados["musica"]:
    recursos_carregados["musica"].play(-1)  # Loop infinito

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.blit(recursos_carregados["fundo"], (0, 0))
    pygame.display.flip()

pygame.quit()