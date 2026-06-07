import time

def calcular_media():

    notas = {
        "Matemática": 0,
        "Português": 0,
        "Geografia": 0,
        "História": 0,
        "Ciências": 0,
        "Educação Física": 0
    }

    print("\nDigite abaixo suas notas: ")

    for materia in list(notas.keys()):
        nota = float(input(f"Nota da {materia}:"))
        notas[materia] = nota
    
    total = sum(notas.values())
    media = total / len(notas)

    print("Calculando a média e verificando seu status...")
    time.sleep(2)

    print("\n--- Resumo final ---")
    print(f"Sua nota total foi :{total:.2f}")
    print(f"Sua média geral foi {media:.2f}")

    if media >= 7:
        print("Parabéns! Você foi aprovado!")
    elif media >= 5:
        print("Você está de recuperação! Precisa melhorar.")
    else:
        print("Loser! Você reprovou!")
    

total_notas = input("Digite seu nome:  ")
calcular_media()
