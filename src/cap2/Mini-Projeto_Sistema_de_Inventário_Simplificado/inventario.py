
def main():
# Variáveis iniciais
    mochila = {
        "flechas": 10,
        "poções de cura": 3,
        "ouro": 50.5
    }
    # Mostra inventário
    print("=== INVENTÁRIO ===")
    for item, quantidade in mochila.items():
        print(f"{item}: {quantidade}")


# Adiciona novo item
    novo_item = input("\nDigite um novo item: ")
    nova_quantidade = input(f"Quantidade de {novo_item}: ")
    # Converte quantidade para número (int ou float)
    if '.' in nova_quantidade:
        nova_quantidade = float(nova_quantidade)
    else:
        nova_quantidade = int(nova_quantidade)
        # Atualiza mochila
        mochila[novo_item] = nova_quantidade
    # Mostra inventário atualizado
        print("\n=== INVENTÁRIO ATUALIZADO ===")
        for item, quantidade in mochila.items():
            print(f"{item}: {quantidade}")
if __name__ == "__main__":
    main()
