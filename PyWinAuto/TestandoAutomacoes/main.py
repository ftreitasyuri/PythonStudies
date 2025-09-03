import tkinter as tk
from tkinter import messagebox

# Função de login simulada
def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario == "SAPUSER" and senha == "1234":
        messagebox.showinfo("Login SAP", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login SAP", "Usuário ou senha inválidos!")

# Criando janela principal
root = tk.Tk()
root.title("SAP Logon")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Labels e Entradas
label_titulo = tk.Label(root, text="SAP Logon", font=("Arial", 14, "bold"), bg="#f0f0f0")
label_titulo.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

label_usuario = tk.Label(frame, text="Usuário:", font=("Arial", 10), bg="#f0f0f0")
label_usuario.grid(row=0, column=0, padx=5, pady=5)
entry_usuario = tk.Entry(frame, font=("Arial", 10))
entry_usuario.grid(row=0, column=1, padx=5, pady=5)

label_senha = tk.Label(frame, text="Senha:", font=("Arial", 10), bg="#f0f0f0")
label_senha.grid(row=1, column=0, padx=5, pady=5)
entry_senha = tk.Entry(frame, show="*", font=("Arial", 10))
entry_senha.grid(row=1, column=1, padx=5, pady=5)

# Botão de login
btn_login = tk.Button(root, text="Login", command=login, bg="#004080", fg="white", font=("Arial", 10, "bold"))
btn_login.pack(pady=15)

# Rodar a interface
root.mainloop()
