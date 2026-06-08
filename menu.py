import curses
import os
import subprocess

# Lista de opções do menu: (Texto que aparece, Nome do arquivo .py)
OPCOES = [
    ("1. Conversão de Temperatura", "conversao_temperatura.py"),
    ("2. Calculadora de Desconto", "desconto.py"),
    ("3. Controle de Estoque", "estoque.py"),
    ("4. Filtro de Idades", "lista_ages.py"),
    ("5. Verificador de Maioridade", "maioridade.py"),
    ("6. Verificador de Múltiplos", "multiplos.py"),
    ("7. Par ou Ímpar", "parImpar.py"),
    ("8. Testes Gerais", "media.py"),
    ("9. Sair do Sistema", None)
]

def desenhar_menu(stdscr, selecao_atual):
    stdscr.clear()
    altura, largura = stdscr.getmaxyx()

    # Título do Menu
    titulo = "=== PAINEL DE TREINAMENTO PYTHON ==="
    stdscr.addstr(1, max(0, (largura - len(titulo)) // 2), titulo, curses.A_BOLD)
    
    instrucoes = "Use as SETAS (↑ / ↓) para navegar e ENTER para selecionar"
    stdscr.addstr(2, max(0, (largura - len(instrucoes)) // 2), instrucoes, curses.A_DIM)
    
    stdscr.addstr(4, 2, "-" * (largura - 4))

    # Desenha as opções
    for idx, (texto, _) in enumerate(OPCOES):
        x = 4
        y = 6 + idx
        
        if idx == selecao_atual:
            # Destaca a linha selecionada invertendo as cores de fundo/texto
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, f" > {texto} ")
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, f"   {texto}")

    stdscr.refresh()

def rodar_menu(stdscr):
    # Configurações do terminal para o curses funcionar bem
    curses.curs_set(0) # Esconde o cursor piscante
    stdscr.keypad(True) # Ativa a captura de teclas especiais (setas)
    
    selecao = 0

    while True:
        desenhar_menu(stdscr, selecao)
        
        # Espera o usuário pressionar uma tecla
        tecla = stdscr.getch()

        if tecla == curses.KEY_UP:
            # Seta para cima: diminui o índice (com trava para não menor que zero)
            selecao = (selecao - 1) % len(OPCOES)
        elif tecla == curses.KEY_DOWN:
            # Seta para baixo: aumenta o índice
            selecao = (selecao + 1) % len(OPCOES)
        elif tecla in [10, 13, curses.KEY_ENTER]:
            # Pressionou Enter
            texto_opcao, arquivo_script = OPCOES[selecao]
            
            if arquivo_script is None:
                # Escolheu "Sair"
                break
                
            # Restaura temporariamente o terminal original para que o script executado
            # possa usar o input() e o print() comuns sem interferência do curses
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            
            # Executa o script selecionado
            print(f"\n[Iniciando: {texto_opcao}]\n")
            if os.path.exists(arquivo_script):
                # Executa o arquivo usando o python3 do sistema
                subprocess.run(["python3", arquivo_script])
            else:
                print(f"Erro: O arquivo '{arquivo_script}' não foi encontrado nesta pasta!")
            
            input("\nPressione ENTER para voltar ao menu...")
            
            # Reinicializa o ambiente do curses para redesenhar o menu
            stdscr = curses.initscr()
            curses.cbreak()
            stdscr.keypad(True)
            curses.noecho()
            curses.curs_set(0)

# Inicializa a aplicação curses de forma segura
curses.wrapper(rodar_menu)
print("\nSistema encerrado com sucesso. Bons estudos!")