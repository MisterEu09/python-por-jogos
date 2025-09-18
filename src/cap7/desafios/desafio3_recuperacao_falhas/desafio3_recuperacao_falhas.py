import json
import sys
from jogo import iniciar_jogo, carregar_estado

def main():
    try:
        estado_atual = iniciar_jogo()
    except Exception as e:
        print(f"ERRO FATAL: {e}. Salvando estado de recuperação...")
        with open("src/cap7/desafios/desafio3_recuperacao_falhas/recovery.sav", "w") as f:
            json.dump(e.estado if hasattr(e, "estado") else {}, f)
        sys.exit(1)

if __name__ == "__main__":
    try:
        with open("src/cap7/desafios/desafio3_recuperacao_falhas/recovery.sav") as f:
            estado = json.load(f)
            print("⚠️ Jogo anterior falhou. Deseja recuperar? (s/n)")
            if input().lower() == "s":
                carregar_estado(estado)
                sys.exit(0)
    except FileNotFoundError:
        pass

    main()