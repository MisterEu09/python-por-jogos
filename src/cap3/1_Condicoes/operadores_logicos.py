tem_chave = True
tem_espada = False
tem_armadura = True


# Condição para abrir o baú: precisa ter a chave E não ter a espada
if tem_chave and not tem_espada:
    print("Abriu o baú! Ganhou uma espada.")
    tem_espada = True


# Condição para entrar na próxima fase: precisa ter a espada OU a armadura
if tem_espada or tem_armadura:
    print("Você pode entrar na próxima fase da jornada.")
