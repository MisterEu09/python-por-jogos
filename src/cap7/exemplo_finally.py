save_file = None
try:
    save_file = open("src/cap7/progresso.dat", "r")
    dados = save_file.read()
except FileNotFoundError:
    print("Save não encontrado!")
finally:
    print("Save encontrado!")
    if save_file is not None:
        save_file.close()  # Fecha o arquivo em QUALQUER caso
    print("Arquivo fechado.")