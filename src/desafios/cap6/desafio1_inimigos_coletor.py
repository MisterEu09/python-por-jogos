def __init__(self):
    # ... código existente …
    self.inimigos = []
    self.cor_inimigo = (220, 20, 60)
def criar_inimigo(self):
    return pygame.Rect(
        random.randint(0, self.LARGURA-30),
        random.randint(0, self.ALTURA-30),
        30, 30
    )


def mover_inimigos(self):
    for inimigo in self.inimigos[:]:
        inimigo.x += random.choice([-2, 0, 2])
        inimigo.y += random.choice([-2, 0, 2])


def verificar_colisoes(self):
    # ... colisões com moedas …
    for inimigo in self.inimigos[:]:
        if self.jogador.colliderect(inimigo):
            self.pontos = max(0, self.pontos - 1)

#Adicione e chame essas funções no loop principal da classe Jogo em C:\Users\miste\OneDrive\Desktop\python-por-jogos\src\cap6\Mini-Projeto_Avançado_Coletorde_Moedas\coletor_moedas\game_loop.py