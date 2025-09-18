
def __init__(self):
    # ... código existente …
    self.nivel = 1


def verificar_colisoes(self):
    # ... colisões existentes …
    if self.pontos % 5 == 0 and self.pontos > 0:
        self.nivel += 1
        self.velocidade += 1
        print(f"⭐ Nível {self.nivel}! Velocidade: {self.velocidade}")



def desenhar_elementos(self):
    # ... desenho existente …
    nivel_texto = self.fonte.render(f"Nível: {self.nivel}", True, self.cores["texto"])
    self.tela.blit(nivel_texto, (self.LARGURA - 150, 20))
# Atualize a exibição do nível na tela na Classe Jogo em C:\Users\miste\OneDrive\Desktop\python-por-jogos\src\cap6\Mini-Projeto_Avançado_Coletorde_Moedas\coletor_moedas\game_loop.py