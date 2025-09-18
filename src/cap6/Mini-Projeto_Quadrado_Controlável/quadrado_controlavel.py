import pygame


# Inicialização
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Controle o Quadrado")
clock = pygame.time.Clock()


# Cores
PRETO = (0, 0, 0)
AZUL = (0, 120, 255)


# Jogador
jogador = pygame.Rect(LARGURA//2, ALTURA//2, 50, 50)
velocidade = 5


# Loop principal
rodando = True
while rodando:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


    # Movimento
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador.left > 0: 
        jogador.x -= velocidade
    if teclas[pygame.K_RIGHT] and jogador.right < LARGURA: 
        jogador.x += velocidade
    if teclas[pygame.K_UP] and jogador.top > 0: 
        jogador.y -= velocidade
    if teclas[pygame.K_DOWN] and jogador.bottom < ALTURA: 
        jogador.y += velocidade
    # Renderização
    tela.fill(PRETO)
    pygame.draw.rect(tela, AZUL, jogador)
    pygame.display.flip()
    # Controle de FPS
    clock.tick(60)
pygame.quit()
