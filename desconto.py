def calcular_desconto(valor_original):

    margem = 0.85
    valor_c_desconto = valor_original * margem
    valor_descontado = valor_original - valor_c_desconto
    
    print(f"O seu desconto foi de R$ {valor_descontado:.2f}")
    print(f"O valor final da sua compra ficou em R$ {valor_c_desconto:.2f}")
    
valor_produto = float(input("Digite o valor da comrpa: R$ "))
calcular_desconto(valor_produto)