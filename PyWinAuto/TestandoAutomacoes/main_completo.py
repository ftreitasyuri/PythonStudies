import tkinter as tk
from tkinter import ttk, messagebox

# Função simulada de login
def login():
    sistema = combo_sistema.get()
    cliente = entry_cliente.get()
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    idioma = entry_idioma.get()

    if usuario == "SAPUSER" and senha == "1234":
        messagebox.showinfo("SAP Logon", f"Login bem-sucedido!\n\nSistema: {sistema}\nCliente: {cliente}\nIdioma: {idioma}")
    else:
        messagebox.showerror("SAP Logon", "Usuário ou senha inválidos!")

# Função para fechar a janela
def cancelar():
    root.destroy()

# Criando janela principal
root = tk.Tk()
root.title("SAP Logon")
root.geometry("400x300")
root.configure(bg="#e6e6e6")

# Frame principal
frame = tk.Frame(root, bg="#e6e6e6")
frame.pack(pady=20)

# Sistema
tk.Label(frame, text="Sistema:", bg="#e6e6e6", font=("Arial", 10)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
combo_sistema = ttk.Combobox(frame, values=["PRD - Produção", "QAS - Qualidade", "DEV - Desenvolvimento"])
combo_sistema.grid(row=0, column=1, padx=5, pady=5)
combo_sistema.current(0)

# Cliente
tk.Label(frame, text="Cliente:", bg="#e6e6e6", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_cliente = tk.Entry(frame)
entry_cliente.grid(row=1, column=1, padx=5, pady=5)
entry_cliente.insert(0, "100")

# Usuário
tk.Label(frame, text="Usuário:", bg="#e6e6e6", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_usuario = tk.Entry(frame)
entry_usuario.grid(row=2, column=1, padx=5, pady=5)

# Senha
tk.Label(frame, text="Senha:", bg="#e6e6e6", font=("Arial", 10)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_senha = tk.Entry(frame, show="*")
entry_senha.grid(row=3, column=1, padx=5, pady=5)

# Idioma
tk.Label(frame, text="Idioma:", bg="#e6e6e6", font=("Arial", 10)).grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_idioma = tk.Entry(frame, width=5)
entry_idioma.grid(row=4, column=1, sticky="w", padx=5, pady=5)
entry_idioma.insert(0, "PT")

# Botões
btn_frame = tk.Frame(root, bg="#e6e6e6")
btn_frame.pack(pady=15)

btn_login = tk.Button(btn_frame, text="Enter", command=login, bg="#004080", fg="white", font=("Arial", 10, "bold"), width=10)
btn_login.grid(row=0, column=0, padx=10)

btn_cancelar = tk.Button(btn_frame, text="Cancelar", command=cancelar, bg="#808080", fg="white", font=("Arial", 10, "bold"), width=10)
btn_cancelar.grid(row=0, column=1, padx=10)

# Rodar a interface
root.mainloop()
