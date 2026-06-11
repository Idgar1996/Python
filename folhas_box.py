def folhas_box():
    largura = int(input("Digite a largura do box: "))
    altura = int(input("Digite a altura do box: "))
    transpasse = int(input("Digite a medida do transpasse desejado: "))
    
    largura_folhas = int((largura + transpasse) / 2)
    altura_movel = int(altura - 25)
    altura_fixo = int(altura - 60)

    print(f"Medidas da folha fixa: {largura_folhas} X {altura_fixo}")
    print(f"Medidas da folha móvel: {largura_folhas} X {altura_movel}")

print("Digite as medidas em milímetros!")
folhas_box()