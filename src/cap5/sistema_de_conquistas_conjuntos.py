#Conjunto de conquistas do jogador
conquistas = {'primeiro_chefe', 'coletor_de_itens'} 
#Adicionando uma nova conquista (se ela já existir, nada acontece)
conquistas.add('primeiro_chefe') 
conquistas.add('mestre_da_espada') 
print(f"Conquistas atuais: {conquistas}") 
#Saída: Conquistas atuais: {'primeiro_chefe', 'coletor_de_itens', 'mestre_da_espada'}
#Verificando se uma conquista foi desbloqueada (operação muito rápida)
if 'coletor_de_itens' in conquistas: print("Você já desbloqueou a conquista de coletor de itens!")
