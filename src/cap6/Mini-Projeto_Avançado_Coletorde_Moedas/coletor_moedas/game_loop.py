import pygame
from jogador import Jogador
from moedas import GerenciadorMoedas

# Classe principal do jogo
class Jogo:
    def __init__(self):
        pygame.init()  # Inicializa o pygame
        self.LARGURA, self.ALTURA = 800, 600  # Define tamanho da tela
        self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA))  # Cria a janela do jogo
        pygame.display.set_caption("Coletor de Moedas")  # Define o título da janela
        self.clock = pygame.time.Clock()  # Relógio para controlar FPS
        
        # Define as cores usadas no jogo
        self.cores = {
            "fundo": (25, 25, 40),
            "texto": (240, 240, 240)
        }
        
        self.jogador = Jogador(self.LARGURA//2, self.ALTURA//2)  # Cria o jogador no centro da tela
        self.moedas = GerenciadorMoedas()  # Gerenciador de moedas
        self.pontos = 0  # Pontuação inicial
        self.fonte = pygame.font.SysFont(None, 36)  # Fonte para exibir pontuação

    # Loop principal do jogo
    def run(self):
        rodando = True
        while rodando:
            # Processa eventos (teclado, fechar janela, etc)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False  # Encerra o jogo se fechar a janela
            
            # Lógica do jogo
            teclas = pygame.key.get_pressed()  # Verifica teclas pressionadas
            self.jogador.mover(teclas, (self.LARGURA, self.ALTURA))  # Move o jogador
            self.moedas.adicionar_moeda((self.LARGURA, self.ALTURA))  # Adiciona moedas
            self.pontos += self.moedas.verificar_colisao(self.jogador.rect)  # Verifica colisão e soma pontos
            
            # Renderização dos elementos na tela
            self.tela.fill(self.cores["fundo"])  # Preenche o fundo
            self.jogador.desenhar(self.tela)  # Desenha o jogador
            self.moedas.desenhar(self.tela)  # Desenha as moedas
            
            # Exibe a pontuação
            texto = self.fonte.render(f"Moedas: {self.pontos}", True, self.cores["texto"])
            self.tela.blit(texto, (20, 20))
            
            pygame.display.flip()  # Atualiza a tela
            self.clock.tick(60)  # Limita FPS a 60
        
        pygame.quit()  # Encerra o pygame

# Executa o jogo se o arquivo for chamado diretamente
if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()
