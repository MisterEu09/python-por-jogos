import pygame

LARGURA, ALTURA = 800, 600
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
FPS = 60

class ErroFatal(Exception):
    def __init__(self, mensagem, estado):
        super().__init__(mensagem)
        self.estado = estado

def iniciar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Plataforma Simples")
    relogio = pygame.time.Clock()

    jogador = pygame.Rect(100, 500, 50, 50)
    velocidade_y = 0
    no_chao = False
    plataforma = pygame.Rect(0, 550, LARGURA, 50)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return {
                    "jogador_x": jogador.x,
                    "jogador_y": jogador.y
                }

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jogador.x -= 5
        if teclas[pygame.K_RIGHT]:
            jogador.x += 5
        if teclas[pygame.K_SPACE] and no_chao:
            velocidade_y = -15
            no_chao = False

        velocidade_y += 1
        jogador.y += velocidade_y

        if jogador.colliderect(plataforma):
            jogador.bottom = plataforma.top
            velocidade_y = 0
            no_chao = True

        # ERRO FATAL: jogador caiu fora da tela
        if jogador.y > ALTURA:
            raise ErroFatal("Jogador caiu!", {
                "jogador_x": jogador.x,
                "jogador_y": jogador.y
            })

        tela.fill(BRANCO)
        pygame.draw.rect(tela, AZUL, jogador)
        pygame.draw.rect(tela, VERDE, plataforma)
        pygame.display.flip()
        relogio.tick(FPS)

def carregar_estado(estado):
    print("🔄 Estado recuperado:", estado)
    # Aqui você poderia usar o estado para reiniciar o jogo com posição salva
    iniciar_jogo()