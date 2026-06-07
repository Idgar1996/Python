def conv_temp_fah(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print(f"A temperatura atual é de {fahrenheit} graus fahrenheit!")

    if fahrenheit > 89.6:
        print("Está muito quente! Refresque-se imediatamente!")
    elif fahrenheit > 50:
        print("A temperatura está agradável")    
    else:
        print("Está muito frio! Aqueca-se imediatamente!")

temperatura = float(input("Digite a temperatura atual: "))
conv_temp_fah(temperatura)