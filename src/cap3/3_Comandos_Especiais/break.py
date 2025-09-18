vidas = 3
while True:  # Loop "infinito"
    print(f"Vidas restantes: {vidas}")
    vidas -= 1
    if vidas == 0:
        print("Sem vidas! Fim de jogo.")
        break  # Sai do loop
