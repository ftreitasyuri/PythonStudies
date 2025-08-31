# Importando tkinter
from tkinter import *


janela = Tk()
janela.title("Label")

# Configurar tamanho
janela.geometry('500x250')

# Cor de fundo da janela
cor = '#242323'
janela.config(background=cor)


# Labels
label_nome = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 10'), fg='#fc3503', bg='yellow')
label_nome.place(x=10, y=10)


nome = Label(janela, width=10, height=2, text='Yuri Dev: ', font=('Arial 10'), fg='#fc3503', bg='yellow')
nome.place(x=100, y=10)




label_idade = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 10'))
label_idade.place(x=10, y=60)

idade = Label(janela, width=10, height=2, text='28 anos', font=('Arial 10'))
idade.place(x=100, y=60)


label_pais = Label(janela, width=10, height=2, text='Pais: ', font=('Arial 10'))
label_pais.place(x=10, y=110)

pais = Label(janela, width=10, height=2, text='Brasil', font=('Arial 10'))
pais.place(x=100, y=110)

janela.mainloop()