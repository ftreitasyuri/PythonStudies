from pywinauto import Application
import pyautogui
import time
# Iniciar Notepad++
app = Application(backend='win32').start(r'"C:\Program Files\Notepad++\notepad++.exe"')
# C:\ProgramData\Microsoft\Windows\Start Menu\Programs

# Conectar com a janela principal
dlg = app.window(title_re=".*novo 1")
# time.sleep(3)

pyautogui.hotkey('win', 'up')

# Listar todas as janelas detectadas pelo pywinauto
# print("=== Janelas Disponíveis ===")
# print(app.windows())

# Lista todos os controles da janela principal
print("=== Controles da janela principal ===")
dlg.print_control_identifiers()

# Digitar um texto
dlg.type_keys("Testando automação com pywinauto no Notepad++{ENTER}", with_spaces=True)

# Abre o menu arquivo e clicar em salvar ou salvar come

# o menu_select vai pegar qualquer menu do sistema baseado no nome informado
dlg.menu_select("Arquivo->Salvar")
# dlg.menu_select("Configurações->Preferências...")

# Selecionando a janela de salvar
win_save = app.window(title_re=".*Salvar *")

# Digitando o nome do $
# win_save["Edit"].type_keys(r'C:\Users\Public\Desktop\meu_primeiro_bot.txt', with_spaces=True)
win_save["Edit"].type_keys(r'C:\Users\yqueiroz\Documents\Pessoal\Python\TestandoAutomacoes\meu_primeiro_bot.txt', with_spaces=True)
# C:\Users\yqueiroz\Documents\Pessoal\Python\TestandoAutomacoes
# 

# Clicar no botão de salvar
win_save["Salvar"].click()

# Usando pyautoGui
pyautogui.hotkey('alt', 'f4')