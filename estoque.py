def atualizar_estoque(item, quantidade):
    
    itens_vendidos = quantidade
    itens = {"parafuso": 100, "martelo": 50, "prego": 200}
    
    if item in itens:
        valor_item = itens[item]
        nova_quantidade = valor_item - itens_vendidos
    
        if itens_vendidos > itens[item]:
            print("Verifique a quantidade vendida, pois ultrapassa a quantidade existente em estoque!")
    
        print(f"Foram vendidos {itens_vendidos} {item}s!")
        print(f"Sobraram {nova_quantidade} {item}s!")
    else:
        print("Item não cadastrado, contate um supervisor!")

item_vendido = input("Digite o item vendido: ")
quantidade_vendida = int(input("Digite a quantidade vendida: "))
atualizar_estoque(item_vendido, quantidade_vendida)