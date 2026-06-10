import time
import pyautogui

# Segurança: Mova o mouse para o canto superior esquerdo da tela para PARAR o script
pyautogui.FAILSAFE = True

print("Script iniciado. Você tem 5 segundos para clicar em cima da primeira ficha da tabela...")
time.sleep(5)

# Defina quantas fichas quer baixar nesta rodada (ex: 30 fichas)
TOTAL_FICHAS = 76 

for i in range(TOTAL_FICHAS):
    print(f"Processando ficha {i+1} de {TOTAL_FICHAS}...")
    
    # Executa os comandos no sistema
    pyautogui.press('f8')
    time.sleep(1)  # Tempo para o sistema abrir a janela de confirmação
    
    pyautogui.press('s')
    time.sleep(1.2)  # Tempo para o sistema processar a baixa e atualizar a grade
    
    # Se o seu sistema NÃO pula para a próxima linha sozinho, 
    # descomente a linha abaixo para apertar a seta para baixo:
    # pyautogui.press('down')

print("Processo concluído.")