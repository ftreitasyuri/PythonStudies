from tkinter import *


janela = Tk()
janela.title("Ola mundo")

# Configurar tamanho
janela.geometry('500x250')

# Cor de fundo da janela
cor = '#242323'
janela.config(background=cor)

# Alterando o icone

janela.iconphoto(False, PhotoImage(file='logo.png'))

# Bloqueando redimensionamente
janela.resizable(width=False, height=False)


# Fim do código
janela.mainloop()