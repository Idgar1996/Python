def atualizar_estoque(item, quantidade):
    
    itens = {"parafuso": 100, "martelo": 50, "prego": 200}
    
    
    if item in itens:
        if quantidade > itens[item]:
            print("A quantidade informada é maior que a quantidade em estoque! Verifique com seu supervisor!")
 
        else:
          itens[item] = itens[item] - quantidade
          print(f"A nova quantidade de {item}s é {itens[item]}")
          print(f"Foram vendidos {quantidade} {item}s!")
        
    else:
        print("O item não está cadastrado no sistema, contate um supervisor!")

item_vendido = input("Digite o item vendido: ")
quantidade_vendida = int(input("Digite a quantidade vendida: "))
atualizar_estoque(item_vendido, quantidade_vendida)