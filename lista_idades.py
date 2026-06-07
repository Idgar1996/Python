def listar_idades(lista_geral):
    
    maior_idade = []
    menor_idade =[]
    
    for item in lista_geral:
        if item >= 18:
            maior_idade.append(item)
        else:
            menor_idade.append(item)
            
    print(maior_idade)
    print(menor_idade)

lista_idades = [14, 26, 18, 12, 35, 40, 17, 22]
listar_idades(lista_idades)