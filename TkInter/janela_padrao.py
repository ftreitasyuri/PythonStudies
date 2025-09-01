from tkinter import *

janela = Tk()
janela.title('Entrada de valores')
janela.geometry("500x450")

# Background Janela
cor = '#242323'
janela.config(background=cor)

# Bloqueando redimensionamento
janela.resizable(width=False, height=False)

# Fim do código
janela.mainloop()