def imparPar(numero):

    if numero % 2 == 0:
        print(f"O número {numero} é par!")
    else:
        print(f"O número {numero} é impar!")

valor = float(input("Digite um número: "))
imparPar(valor)
