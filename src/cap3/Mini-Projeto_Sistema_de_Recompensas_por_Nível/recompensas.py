def main():
    print("🏆 SISTEMA DE RECOMPENSAS 🏆")
    nivel = int(input("Digite seu nível: "))
    
    # Validação de entrada
    while nivel < 1 or nivel > 100:
        print("Nível inválido! Deve ser entre 1 e 100.")

        nivel = int(input("Tente novamente: "))
    
    # Verificação hierárquica de recompensas
    if nivel >= 80:
        print("Recompensa: Armadura de Dragão + Espada Épica!")
    elif nivel >= 50:
        print("Recompensa: Arco Élfico + 100 flechas de gelo!")
    elif nivel >= 20:
        print("Recompensa: Machado Duplo + Poção de Invisibilidade!")
    elif nivel >= 5:
        print("Recompensa: Adaga Afiada + 5 poções de cura!")
    else:
        print("Recompensa: Faca Básica + 1 poção de cura.")
    
    # Bônus para níveis altos
    if nivel > 90:
        print("✨ BÔNUS: Asas Angelicais desbloqueadas!")


if __name__ == "__main__":
    main()

