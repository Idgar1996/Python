import json

with open("erro/erro.js", "r", encoding="UTF-8") as arq:
       infos = json.load(arq)

def opcoes(escolha):
    if escolha == 1:
           novo_cadastro();


def novo_cadastro(nome, problema, status):

            with open ("erro/erro.json", "w", encoding="UTF-8") as arq:
                cadastro = json.load(arq)
                novo_id = len(cadastro) + 1
                print(f"O novo id é {novo_id}")
            nome = input("Nome do Cliente: ")
            problema = input("Problema relatado: ")
            status = "aberto",

            with open("erro/erro.json", "r", encoding="UTF-8") as arq:
                   json.dump(cadastro, arq, indent=4, ensure_ascii=False)


chamada = int(input("Digite 1 para novo, 2 para listar erros e 3 para atualizar status."))
opcoes(chamada)