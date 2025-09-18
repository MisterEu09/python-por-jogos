import pygame

# Classe que representa o jogador
class Jogador:
    def __init__(self, x, y, tamanho=40, velocidade=5):
        # Cria um retângulo para representar o jogador na tela
        self.rect = pygame.Rect(x, y, tamanho, tamanho)
        # Define a velocidade de movimento do jogador
        self.velocidade = velocidade
        # Define a cor do jogador (RGB)
        self.cor = (50, 200, 100)
    
    # Método para mover o jogador conforme as teclas pressionadas e os limites da tela
    def mover(self, teclas, limites_tela):
        # Move para a esquerda se a tecla correspondente estiver pressionada e não ultrapassar o limite esquerdo
        if teclas[pygame.K_LEFT] and self.rect.left > 0: 
            self.rect.x -= self.velocidade
        # Move para a direita se a tecla correspondente estiver pressionada e não ultrapassar o limite direito
        if teclas[pygame.K_RIGHT] and self.rect.right < limites_tela[0]: 
            self.rect.x += self.velocidade
        # Move para cima se a tecla correspondente estiver pressionada e não ultrapassar o limite superior
        if teclas[pygame.K_UP] and self.rect.top > 0: 
            self.rect.y -= self.velocidade
        # Move para baixo se a tecla correspondente estiver pressionada e não ultrapassar o limite inferior
        if teclas[pygame.K_DOWN] and self.rect.bottom < limites_tela[1]: 
            self.rect.y += self.velocidade

    # Método para desenhar o jogador na tela
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)
