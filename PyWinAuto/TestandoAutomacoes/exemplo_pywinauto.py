from pywinauto import Application
import time

# Abre o SAP Logon
app = Application(backend="uia").start(r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe")

# Conecta na janela principal
dlg = app.window(title_re="SAP Logon*")

# Espera a janela carregar
dlg.wait("visible", timeout=20)

# Exemplo: Selecionar um sistema da lista (primeiro da lista)
sistema = dlg.child_window(title="PRD", control_type="ListItem")
sistema.click_input(double=True)

# Agora a janela de login aparece
login_win = app.window(title_re="SAP")

# Espera a tela de login abrir
login_win.wait("visible", timeout=20)

# Preenche os campos
login_win.child_window(auto_id="100", control_type="Edit").type_keys("SAPUSER")   # Usuário
login_win.child_window(auto_id="101", control_type="Edit").type_keys("1234")      # Senha
login_win.child_window(auto_id="102", control_type="Edit").type_keys("100")       # Cliente
login_win.child_window(auto_id="103", control_type="Edit").type_keys("PT")        # Idioma

# Pressiona Enter para logar
login_win.type_keys("{ENTER}")

time.sleep(3)
