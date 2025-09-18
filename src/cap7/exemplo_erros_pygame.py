import pygame


def carregar_imagem_segura(caminho, tamanho_padrao=(50, 50)):
    """Carrega uma imagem com fallback para placeholder"""
    try:
        return pygame.image.load(caminho)
    except pygame.error:
        print(f"⚠️ Imagem {caminho} não encontrada! Usando placeholder.")
        superficie = pygame.Surface(tamanho_padrao)
        superficie.fill((255, 0, 255))  # Magenta (cor de erro)
        return superficie


def main():
    """Loop principal à prova de erros"""
    try:
        # Inicialização do Pygame
        pygame.init()
        tela = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Jogo com Tratamento de Erros")
        clock = pygame.time.Clock()
        
        # Carregar recursos
        imagem = carregar_imagem ("assets/images/personagem.png")

        
        # Loop principal
        executando = True
        while executando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    executando = False
            
            # Lógica do jogo e renderização
            tela.fill((0, 0, 0))
            tela.blit(imagem, (400, 300))
            pygame.display.flip()
            clock.tick(60)
            
    except pygame.error as e:
        print(f"❌ ERRO GRAVE NO PYGAME: {e}")
    except Exception as e:
        print(f"❌ ERRO INESPERADO: {type(e).__name__} - {e}")
    finally:
        pygame.quit()  # Garante que o Pygame será fechado


if __name__ == "__main__":
    main()
