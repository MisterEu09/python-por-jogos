# Variável global que representa a quantidade de ouro do jogador
ouro = 100

def comprar_item(preco):
    # Declaração obrigatória para modificar a variável global 'ouro'
    global ouro 
    
    # Subtrai o preço do item do saldo de ouro
    ouro = ouro - preco
    
    # Exibe mensagem informando que a compra foi realizada e mostra o saldo atual
    print(f"Compra realizada! Saldo: {ouro}")

# Exemplo de compra de um item que custa 30 de ouro
comprar_item(30)
