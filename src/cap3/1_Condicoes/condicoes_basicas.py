print("=== SISTEMA DE CLASSIFICAÇÃO ===")


pontuacao = int(input("Digite sua pontuação: "))

if pontuacao >= 1000:
    print("Classificação: Lendário")
elif pontuacao >= 500:
    print("Classificação: Mestre")
elif pontuacao >= 100:
    print("Classificação: Veterano")
else:
    print("Classificação: Iniciante")


print("\n=== VERIFICAÇÃO DE ACESSO ===")
idade = int(input("Digite sua idade: "))
tem_cartao = input("Tem cartão membro? (s/n): ").lower() == 's'


if idade >= 18 and tem_cartao:
    print("Acesso VIP liberado!")
elif idade >= 18:
    print("Acesso regular liberado")
else:
    print("Acesso negado - menor de idade")
