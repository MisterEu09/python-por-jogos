# Define a função para criar um inimigo com tipo e vida padrão
def criar_inimigo(tipo="Goblin", vida=50):
    # Exibe mensagem informando o tipo e vida do inimigo criado
    print(f"✨ {tipo} apareceu com {vida} de HP!")
    # Retorna um dicionário representando o inimigo
    return {"tipo": tipo, "vida": vida}

# Cria um inimigo usando os valores padrão (tipo: Goblin, vida: 50)
inimigo1 = criar_inimigo()  
# ✨ Goblin apareceu com 50 de HP!

# Cria um inimigo sobrescrevendo os valores padrão (tipo: Orc, vida: 80)
inimigo2 = criar_inimigo("Orc", 80)  
# ✨ Orc apareceu com 80 de HP!
