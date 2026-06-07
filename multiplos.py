def verificar_multiplos(num1, num2):
    
    achou_multiplo = False
    
    if num1 % num2 == 0 :
        print(f"O primeiro valor {num1} é múltiplo do segundo valor, {num2}.")
        achou_multiplo = True
        
    if num2 % num1 ==0 and num1 != num2:
        print(f"O segundo valor {num2} é multiplo do primeiro valor, {num1}")
        achou_multiplo = True
        
    if not achou_multiplo:
        print("Nenhum número é múltiplo de nenhum!")
        
valorUm = int(input("Digite um valor inteiro: "))
valorDois = int(input("Digite outro valor inteiro: "))
verificar_multiplos(valorUm, valorDois)