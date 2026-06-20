from pathlib import Path
import time

regras_organizacao = {
    "imagens": [".jpeg", ".jpg", ".png", ".gif"],
    "documentos": [".pdf", ".txt", ".docx", ".xlsx"],
    "compactados": [".zip", ".rar"],
    "executaveis": [".exe", ".msi"],
    "programacao": [".py", ".js", ".css", ".html", ".php", ".json", ]
}

def mapear_diretorio(caminho_alvo):
    diretorio = Path(caminho_alvo)

    if not diretorio.exists() or not diretorio.is_dir():
        print(f"Erro! O caminho '{caminho_alvo}' não é um diretório válido!")
        print("Digite um caminho válido!")
        return
    
    print(f"Lendo arquivos em {diretorio.absolute()}\n")
    
    time.sleep(2)

    contadores = {
          ".jpeg": 0, ".jpg": 0, ".png": 0, ".gif": 0,
          ".pdf": 0, ".txt": 0, ".docx": 0, ".xlsx": 0,
          ".zip": 0, ".rar": 0, ".exe": 0, ".msi": 0,
          ".py": 0, ".js": 0, ".css": 0, ".html": 0,
          ".php": 0, ".json": 0
    }

    total_pastas = 0

    for item in diretorio.iterdir():
        if item.is_file():
            
            extensao = item.suffix.lower()

            if extensao in contadores:
                contadores[extensao] += 1
        elif item.is_dir():
            total_pastas += 1

    print("\n--- Resumo da pasta ---")

    for ext, total in contadores.items():
        if total > 0:
            print(f"Existe um total de {total} arquivos {ext} na pasta {diretorio}.")
        else:
            print(f"Não existem arquivos {ext} na pasta!")
        
    print(f"Existe um  total de {total_pastas} pasta(s) em {diretorio}")

    print("--- Iniciando movimentação dos arquivos ---")

    for item in diretorio.iterdir():
        if item.is_file():
            
            extensao = item.suffix.lower()

            for pasta_nome, extensoes_permitidas in regras_organizacao.items():
                if extensao in extensoes_permitidas:
                    pasta_destino = diretorio / pasta_nome

                    pasta_destino.mkdir(parents=True, exist_ok=True)

                    try:
                        novo_caminho = pasta_destino / item.name
                        item.rename(novo_caminho)
                        print(f"Sucesso: arquivo {item.name} movido para a pasta {pasta_nome}")
                    except:
                        print(f"Não foi possível mover o item {item.name} para a pasta {pasta_nome}")

                    break

caminho_teste = input("Digite o caminho da pasta: ")
mapear_diretorio(caminho_teste)