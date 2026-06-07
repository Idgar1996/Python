def maioridade(ano_nascimento):
    ano_atual = 2026
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        print(f"Sua idade é {idade}, então já é de maior!")
    else:
        print(f"Sua idade é {idade}, então ainda é de menor!")

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
maioridade(ano_nascimento)
