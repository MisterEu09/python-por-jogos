for numero in range(1, 6):
    if numero == 3:
        print("Pulando o número 3!")
        continue  # Pula para o próximo número
    print(f"Número: {numero}")
print("Fim do loop.")