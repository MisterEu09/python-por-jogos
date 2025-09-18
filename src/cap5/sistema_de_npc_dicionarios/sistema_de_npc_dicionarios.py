import time
import random

# Dados do NPC e do Jogador
# Define um dicionário para o NPC mercador com nome, diálogo e itens à venda
npc_mercador = {
    "nome": " Geraldo, o Mercador",
    "dialogo": "Bem-vindo à minha loja de relíquias e suprimentos",
    "itens_venda": {
        "Poção de Cura": 50,
        "Flechas": 10,
        "Mapa Antigo": 200
    }
}

# Define um dicionário para o jogador com nome, quantidade de ouro e inventário
jogador = {
    "nome": "Aventureiro", 
    "ouro": 100,
    "inventario": []
}

# Boas Vindas
# Exibe mensagem de boas-vindas do NPC ao jogador
print(f"\n[{npc_mercador['nome']}] Olá, {jogador['nome']}!!")
time.sleep(1)
print(f"[{npc_mercador['nome']}] {npc_mercador['dialogo']}")
time.sleep(1)

# Itens à venda
# Lista os itens disponíveis na loja do NPC
print("\n [ITENS DISPONÍVEIS NA LOJA]")
for item, preco in npc_mercador["itens_venda"].items():
    print(f" - {item}: {preco} moedas")
time.sleep(1)

# Status do jogador
# Mostra o status atual do jogador: ouro e inventário
print("\n [SEU STATUS]")
print(f"Ouro: {jogador['ouro']} moedas")
print(f" Inventário: {jogador['inventario'] if jogador['inventario'] else 'Vazio'}")
time.sleep(1)

# Tentativa de compra
# Seleciona aleatoriamente um item da loja para o jogador tentar comprar
item_escolhido = random.choice(list(npc_mercador["itens_venda"].keys()))
preco_item = npc_mercador["itens_venda"][item_escolhido]

print(f"\n Tentando comprar '{item_escolhido}' por {preco_item} moedas....")
time.sleep(1)

# Verifica se o jogador tem ouro suficiente para comprar o item
if jogador["ouro"] >= preco_item:
    jogador["ouro"] -= preco_item  # Deduz o valor do item do ouro do jogador
    jogador["inventario"].append(item_escolhido)  # Adiciona o item ao inventário
    print("\n Transação bem-sucedida!!")
    print(f"Você adquiriu: {item_escolhido}")
    print(f"Ouro restante: {jogador['ouro']} moedas")
    print(f"Novo inventário: {jogador['inventario']}")
else:
    # Caso não tenha ouro suficiente, informa o jogador
    print("\n Transação falhou!")
    print("Você não tem ouro suficiente para essa compra.")
    print(f"Seu ouro atual: {jogador['ouro']} moedas")
time.sleep(1)

# Encerramento
# Mensagem final de despedida do NPC
print("\n Obrigado por visitar a loja do Geraldo! :)")
print("Boa sorte em sua jornada, aventureiro!!!")
