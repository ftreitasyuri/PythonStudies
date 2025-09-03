# Importações
import pywinauto, time
from pywinauto import Application, keyboard
from pywinauto.keyboard import send_keys

# Estanciando word
# winword = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
# winword = r"C:\Users\yqueiroz\AppData\Local\DBeaver.exe"

# Caminho do Bdeaver
db = r'C:\Users\yqueiroz\AppData\Local\DBeaver\dbeaver.exe'
app = Application(backend="uia").start(db)
time.sleep(2)

# Conecta na janela principal
dlg = app.window(title_re=".*Dbeaver.*")
dlg.wait("visible", timeout=20)
dlg.set_focus() # garante foco na janela principal
time.sleep(0.5)

# Abre menu Database e new database
dlg.type_keys("^+n")
# send_keys("n")
time.sleep(2)