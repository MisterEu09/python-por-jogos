# Banco de dados de receitas
RECEITAS = {
    "espada flamejante": {"aço": 3, "rubi": 1, "carvão": 5},
    "poção de cura forte": {"poção de cura": 2, "cristal azul": 1},
    "arco élfico": {"madeira nobre": 4, "corda resistente": 2}
}
# Inventário do jogador
inventario = {
    "aço": 5,
    "rubi": 2,
    "carvão": 8,
    "poção de cura": 3,
    "cristal azul": 1
}
def verificar_crafting(item):
    """Verifica se o jogador pode craftar o item"""
    
    if item not in RECEITAS:
        print(f"❌ Receita desconhecida: {item}")
        return False
        
    for material, quantidade in RECEITAS[item].items():
        # Usa .get() para evitar KeyError
        if inventario.get(material, 0) < quantidade:
            print(f"❌ Faltam {quantidade - inventario.get(material, 0)} {material}")
            return False
            
    return True
def craftar(item):
    """Realiza o crafting do item"""
    if not verificar_crafting(item):
        return False



    
# Remover materiais
    for material, quantidade in RECEITAS[item].items():
        inventario[material] -= quantidade
        if inventario[material] == 0:
            del inventario[material]
    # Adicionar item craftado
    inventario[item] = inventario.get(item, 0) + 1
    print(f"✨ {item} craftado com sucesso!")
    return True


# Interface de crafting
def menu_crafting():
    print("\n=== 🔨 OFICINA DE CRAFTING ===")
    print("Receitas disponíveis:")
    for i, item in enumerate(RECEITAS, 1):
        materiais = ", ".join([f"{qtd}x {mat}" for mat, qtd in RECEITAS[item].items()])
        print(f"{i}. {item} ({materiais})")
    
    escolha = input("\nO que deseja craftar? (número ou 'sair'): ")
    
    if escolha.lower() == "sair":
        return False
    
    try:
        item_escolhido = list(RECEITAS)[int(escolha)-1]
        craftar(item_escolhido)
    except (ValueError, IndexError):
        print("❌ Escolha inválida!")
    return True


# Loop principal
while menu_crafting():
    print("\nInventário atual:")
    for item, qtd in inventario.items():
        print(f"- {item}: {qtd}")
