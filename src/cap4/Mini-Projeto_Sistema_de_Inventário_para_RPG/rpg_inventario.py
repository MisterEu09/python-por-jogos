# Função para exibir o inventário formatado
def mostrar_inventario(inventario):
    """Exibe itens formatados"""
    print("\n=== 🎒 INVENTÁRIO ===")
    for i, item in enumerate(inventario, 1):  # Enumera os itens a partir de 1
        print(f"{i}. {item.capitalize()}")    # Exibe cada item com a primeira letra maiúscula
    print("=====================")

# Função para adicionar um item ao inventário
def adicionar_item(inventario):
    item = input("Nome do item: ").strip()    # Solicita o nome do item ao usuário
    if item:                                  # Verifica se o nome não está vazio
        inventario.append(item)               # Adiciona o item à lista
        print(f"⭐ {item} adicionado!")
    else:
        print("❌ Nome inválido!")            # Mensagem de erro para nome vazio

# Função para remover um item do inventário
def remover_item(inventario):
    item = input("Item a remover: ").strip()  # Solicita o nome do item a remover
    if item in inventario:                    # Verifica se o item existe no inventário
        inventario.remove(item)               # Remove o item da lista
        print(f"➖ {item} removido!")
    else:
        print(f"❌ {item} não encontrado!")   # Mensagem de erro se o item não existir

# Função principal do programa
def main():
    inventario = ["espada", "poção de cura", "mapa"]  # Inventário inicial
    
    while True:                                       # Loop principal do menu
        print("\nO que fazer?")
        print("1. Ver inventário")
        print("2. Adicionar item")
        print("3. Remover item")
        print("4. Sair")
        
        escolha = input("> ")                         # Recebe a escolha do usuário
        
        if escolha == "1":
            mostrar_inventario(inventario)            # Exibe o inventário
        elif escolha == "2":
            adicionar_item(inventario)                # Adiciona um item
        elif escolha == "3":
            remover_item(inventario)                  # Remove um item
        elif escolha == "4":
            print("Inventário fechado!")              # Sai do programa
            break
        else:
            print("Opção inválida!")                  # Mensagem para opção inválida

# Executa o programa se o arquivo for executado diretamente
if __name__ == "__main__":
    main()
