inventario = {"poção": 3, "flecha": 10}

def usar_item(item, qtd=1):
    if inventario.get(item, 0) >= qtd:
        inventario[item] -= qtd
        if inventario[item] == 0:
            del inventario[item]
        return True
    return False

def mostrar_inventario():
    print("\n📦 Inventário:")
    if not inventario:
        print("  (vazio)")
    else:
        for item, qtd in inventario.items():
            print(f"  {item}: {qtd}")
    print()

def adicionar_item():
    item = input("Digite o nome do item a adicionar: ").strip()
    if not item:
        print("Nome inválido.")
        return
    try:
        qtd = int(input(f"Quantidade de '{item}': "))
        if qtd <= 0:
            print("Quantidade deve ser positiva.")
            return
        inventario[item] = inventario.get(item, 0) + qtd
        print(f"✅ Adicionado {qtd}x '{item}' ao inventário.")
    except ValueError:
        print("Quantidade inválida.")

def remover_item():
    item = input("Digite o nome do item a remover: ").strip()
    if item in inventario:
        del inventario[item]
        print(f"❌ '{item}' removido do inventário.")
    else:
        print("Item não encontrado.")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Mostrar inventário")
        print("2. Adicionar item")
        print("3. Usar item")
        print("4. Remover item")
        print("5. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            mostrar_inventario()
        elif escolha == "2":
            adicionar_item()
        elif escolha == "3":
            item = input("Item a usar: ").strip()
            try:
                qtd = int(input("Quantidade a usar: "))
                if usar_item(item, qtd):
                    print(f"🧪 Usou {qtd}x '{item}'.")
                else:
                    print("❌ Não há quantidade suficiente ou item inexistente.")
            except ValueError:
                print("Quantidade inválida.")
        elif escolha == "4":
            remover_item()
        elif escolha == "5":
            print("👋 Saindo...")
            break
        else:
            print("Opção inválida.")

# Inicia o menu
menu()
# Exemplo de interação:
# === MENU ===
# 1. Mostrar inventário
# 2. Adicionar item
# 3. Usar item
# 4. Remover item
# 5. Sair
# Escolha uma opção: 1
# 📦 Inventário
#  poção: 3
#  flecha: 10
# Escolha uma opção: 2
# Digite o nome do item a adicionar: escudo
# Quantidade de 'escudo': 1
# ✅ Adicionado 1x 'escudo' ao inventário.
# Escolha uma opção: 3
# Item a usar: poção
# Quantidade a usar: 2
# 🧪 Usou 2x 'poção'.
# Escolha uma opção: 1
# 📦 Inventário
#  poção: 1
#  flecha: 10
#  escudo: 1
# Escolha uma opção: 5
# 👋 Saindo...
