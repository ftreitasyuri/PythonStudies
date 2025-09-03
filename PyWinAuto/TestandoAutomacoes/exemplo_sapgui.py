import win32com.client
import time

# Conecta ao SAP GUI
sap_gui_auto = win32com.client.GetObject("SAPGUI")
if not sap_gui_auto:
    raise Exception("SAP GUI não encontrado")

application = sap_gui_auto.GetScriptingEngine

# Seleciona a primeira conexão aberta (ou crie uma nova)
connection = application.Children(0)  # pode variar se tiver múltiplas conexões
session = connection.Children(0)     # a primeira sessão

# --- Login ---
# Preenche usuário
session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "SEU_USUARIO"

# Preenche senha
session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "SUA_SENHA"

# Pressiona Enter para logar
session.findById("wnd[0]").sendVKey(0)

# --- Opcional: esperar a tela inicial carregar ---
time.sleep(2)

# --- Exemplo: abrir transação (opcional) ---
# session.findById("wnd[0]/tbar[0]/okcd").text = "SE16N"
# session.findById("wnd[0]").sendVKey(0)

print("Login realizado com sucesso!")
