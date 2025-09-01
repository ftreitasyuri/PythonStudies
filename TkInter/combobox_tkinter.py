from tkinter import ttk
# Para usar o combobox precisa usar a linha abaixo para import
import tkinter

janela = tkinter.Tk()
janela.title('Combobox')
janela.geometry("500x450")

# Background Janela
cor = '#242323'
janela.config(background=cor)

# Bloqueando redimensionamento
janela.resizable(width=False, height=False)

# Label nome
# label_escolha = Label(janela, width=15, height=2, text='Faça sua escolha', fg='#fff', bg=cor, anchor='w')
label_escolha = ttk.Label(janela, width=15, height=2, text='Faça sua escolha', fg='#fff', bg=cor, anchor='w')
label_escolha.place(x=10, y=20)

# # Combobox
# combo = Combobox(janela)
# combo['values'] = (1, 2, 3, 4,'5')

# combo.place(x=10, y=60)


# Fim do código
janela.mainloop()