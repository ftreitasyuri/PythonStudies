from tkinter import *

janela = Tk()
janela.title('Entrada de valores')
janela.geometry("500x450")

# Background Janela
cor = '#242323'
janela.config(background=cor)

# Bloqueando redimensionamento
janela.resizable(width=False, height=False)

# Entre

label_nome = Label(janela, width=10, height=2, text='Nome')
label_nome.place(x=10, y=20)

# Fim do código
janela.mainloop()