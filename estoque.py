import json

with open("estoque.json", "r", encoding="UTF-8") as arq:
    itens = json.load(arq)

def menu(acao):
    
    if acao == "vender":
        item_vendido = input("Digite o item vendido: ").strip().lower()
        quantidade_vendida = int(input("Digite a quantidade vendida: "))
        venda(item_vendido, quantidade_vendida, itens)
        
    elif acao == "comprar":
        item_comprado = input("Digite o item comprado: ")    
        quantidade_comprada = int(input("Digite a quantidade comprada: ")).strip().lower()
        compra(item_comprado, quantidade_comprada)
        
    else:
        print("Opção inválida! Escolha somente entre as opções disponíveis!")
        
def venda(item, quantidade, itens):
    
    if item in itens:
        if quantidade > itens[item]:
            print("A quantidade informada é maior que a quantidade em estoque! Verifique com seu supervisor!")
 
        else:
          itens[item] = itens[item] - quantidade
          with open("estoque.json", "w", encoding="UTF-8") as arq:
            json.dump(itens, arq, indent=4, ensure_ascii=False)
            
          print(f"A nova quantidade de {item}s é {itens[item]}")
          print(f"Foram vendidos {quantidade} {item}s!")
        
    else:
        print("O item não está cadastrado no sistema, contate um supervisor!")

def compra (item, quantidade, itens):
    if item in itens:
        itens[item] = itens[item] + quantidade
        with open("estoque.json", "w", encoding="UTF-8") as arq:
            json.dump(itens, arq, indent=4, ensure_ascii=False)

        print(f"A nova quantidade de {item} é de {itens[item]}!")
        print(f"Foram comprados {quantidade} {item}s!")
        
    else:
        print("O item não está cadastrado no sistema, peça ao seu supervisor para cadastrar! ")

chamada = input("Digite 'comprar' para adicionar um item, ou, digite 'vender' para vender um item já cadastrado: ").strip().lower()
menu(chamada)
