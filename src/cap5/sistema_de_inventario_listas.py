#Criando uma lista de itens do inventário
inventario = ['espada', 'escudo', 'poção de cura'] 
#Acessando elementos pelo índice (o primeiro índice é 0)
print(inventario[0]) # Saída: espada 
#Alterando um elemento
inventario[1] = 'armadura de ferro' 
print(inventario) # Saída: ['espada', 'armadura de ferro', 'poção de cura'] 
#Adicionando um novo elemento no final
inventario.append('amuleto') 
print(inventario) # Saída: ['espada', 'armadura de ferro', 'poção de cura', 'amuleto'] 
#Removendo um elemento
inventario.remove('espada') 
print(inventario) # Saída: ['armadura de ferro', 'poção de cura', 'amuleto'] 
