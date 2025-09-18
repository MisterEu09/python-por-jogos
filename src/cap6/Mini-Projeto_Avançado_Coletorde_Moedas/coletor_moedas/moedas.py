import pygame
import random

class GerenciadorMoedas:
    def __init__(self):
        # Lista para armazenar as moedas presentes na tela
        self.moedas = []
        # Cor das moedas (dourado)
        self.cor = (255, 215, 0)

    def criar_moeda(self, limites_tela):
        # Cria uma moeda em uma posição aleatória dentro dos limites da tela
        return pygame.Rect(
            random.randint(20, limites_tela[0]-40),  # Posição X aleatória
            random.randint(20, limites_tela[1]-40),  # Posição Y aleatória
            25, 25                                   # Tamanho da moeda
        )
    
    def adicionar_moeda(self, limites_tela, chance=0.02):
        # Adiciona uma nova moeda com uma certa chance a cada chamada
        if random.random() < chance:
            self.moedas.append(self.criar_moeda(limites_tela))
    
    def verificar_colisao(self, jogador_rect):
        # Verifica se o jogador colidiu com alguma moeda
        pontos = 0
        for moeda in self.moedas[:]:  # Itera sobre uma cópia da lista
            if jogador_rect.colliderect(moeda):
                self.moedas.remove(moeda)  # Remove a moeda coletada
                pontos += 1                # Incrementa os pontos
        return pontos
    
    def desenhar(self, tela):
        # Desenha todas as moedas na tela
        for moeda in self.moedas:
            pygame.draw.ellipse(tela, self.cor, moeda)
