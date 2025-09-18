import logging


logging.basicConfig(filename='debug.log', level=logging.DEBUG)


try:
    idade = int(input("Idade: "))
except ValueError as e:
    logging.error(f"ValueError: {e}")
    print("Erro: idade deve ser um número!")
