# Importando tkinter
from tkinter import *


janela = Tk()
janela.title("Label")

# Configurar tamanho
janela.geometry('500x250')

# Cor de fundo da janela
cor = '#242323'
janela.config(background=cor)

# Alterando o icone

janela.iconphoto(False, PhotoImage(file='logo.png'))

# Bloqueando redimensionamente
janela.resizable(width=False, height=False)


# Criando label
cor_label = '#fc3503'
label_nome = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 15 bold'), fg=cor_label, bg=cor)
label_nome.grid(row=0, column=0, pady=10)

label_idade = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 15 bold'))
label_idade.grid(row=1, column=0, pady=10)

label_pais = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 15 bold'))
label_pais.grid(row=2, column=0, pady=10)

# Fim do código
janela.mainloop()