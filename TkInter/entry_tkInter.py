from tkinter import *

janela = Tk()
janela.title('Entrada de valores')
janela.geometry("500x450")

# Função obter dados dos entry

def obter_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    # print(nome, idade, pais)
    nome_resp['text'] = nome
    idade_resp['text'] = idade
    pais_resp['text'] = pais
    
    entry_nome.delete(0,END)
    entry_idade.delete(0,END)
    entry_pais.delete(0,END)
    
def limpar_dados():
    nome_resp['text'] = ''
    idade_resp['text'] = ''
    pais_resp['text'] = ''

# Background Janela
cor = '#242323'
janela.config(background=cor)

# Bloqueando redimensionamento
janela.resizable(width=False, height=False)

# ______________________________________________________________________
# Label nome
label_nome = Label(janela, width=10, height=2, text='Nome', fg='#fff', bg=cor, anchor='w')
label_nome.place(x=10, y=20)

# Entry
entry_nome = Entry(janela, width=10, font=('Arial 20'))
entry_nome.place(x=100, y=20)
# ______________________________________________________________________
# Label idade
label_idade = Label(janela, width=10, height=2, text='Idade', fg='#fff', bg=cor, anchor='w')
label_idade.place(x=10, y=60)

# Entry
entry_idade = Entry(janela, width=10, font=('Arial 20'))
entry_idade.place(x=100, y=60)

# ______________________________________________________________________
# Label pais
label_pais = Label(janela, width=10, height=2, text='País', fg='#fff', bg=cor, anchor='w')
label_pais.place(x=10, y=100)

# Entry
entry_pais = Entry(janela, width=10, font=('Arial 20'), state='disabled')
entry_pais.place(x=100, y=100)

# Botão

botao = Button(janela, command=obter_dados, width=30, height=3, text='Enviar') 
botao.place(x=10, y=150)

botao_limpar = Button(janela, command=limpar_dados, width=30, height=3, text='Limpar Dados') 
botao_limpar.place(x=240, y=150)

# ______________________________________________________________________
# INÍCIO Respostas

nome_resp = Label(janela, width=30, height=2, text='')
nome_resp.place(x=270, y=20)

idade_resp = Label(janela, width=30, height=2, text='')
idade_resp.place(x=270, y=60)

pais_resp = Label(janela, width=30, height=2, text='')
pais_resp.place(x=270, y=100)
# ______________________________________________________________________
# FIM Respostas



# Fim do código
janela.mainloop()