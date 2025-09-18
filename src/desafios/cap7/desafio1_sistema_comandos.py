
import logging
logging.basicConfig(filename='erros.log', level=logging.ERROR)

comandos_validos = {"atacar", "mover", "defender"}
	
while True:
    try:
        comando = input("Comando: ").lower()
        if comando not in comandos_validos:
            raise ValueError(f"Comando inválido: {comando}")


    # Processar comando…        
    except ValueError as e:
        logging.error(str(e))
        print("Erro: Use 'atacar', 'mover' ou 'defender'")
