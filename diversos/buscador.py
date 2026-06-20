usuarios = [
        {"nome": "Gean", "cidade": "Bom Principio"},
        {"nome": "Alice", "cidade": "Porto Alegre"},
        {"nome": "Junior", "cidade": "Caçador"},
        {"nome": "Elieber", "cidade": "Itapema"}
]

def localizar_usuario(cidade):

    encontrou = False

    for pessoa in usuarios:
        if pessoa["cidade"].lower() == cidade.lower():
            print(f"O usuário escolhido foi: {pessoa['nome']}")
            encontrou = True
        
    if not encontrou:
        print("Usuário e cidade não cadastrados")
        
def cadastrar_usuario():
    novo_nome = input("Digite seu nome: ").strip()
    nova_cidade = input("Digite sua cidade: ").strip()
    
    novo_registro = {"nome": novo_nome, "cidade": nova_cidade}
    
    usuarios.append(novo_registro)
    print(f"Usuário {novo_nome} registrado com sucesso!")

menu = input("Digite NOVO para cadastrar um novo usuário, ou BUSCAR para buscar no nosso banco de dados: ").upper()

if menu == "BUSCAR":
    cidade_escolhida = input("Digite a cidade escolhida: ").lower()
    localizar_usuario(cidade_escolhida)

elif menu == "NOVO":
    cadastrar_usuario()
    
else:
    print("Opção inválida!")
    
    
print(usuarios)