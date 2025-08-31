from tkinter import *

janela = Tk()
janela.title('Botão')
janela.geometry("300x250")

# Função apresenta texto
global contador
contador = 0

def executar():
    
    global contador
    
    texto1 = 'Número Impar'
    texto2 = 'Número Par'
    
    if (contador %2) == 0:
        resultado = texto2 + str(contador)
        label['text'] = resultado
        label['fg'] = 'green'
        # print(texto2)
    else:
        resultado = texto1 + str(contador)
        # print(texto1)
        label['text'] = resultado
        label['fg'] = 'yellow'
    contador+=1

    return resultado



# Label
label = Label(janela, width=20, height=2, text='Texto sera apresentado', relief="ridge", fg='white', bg='black')
label.grid(row=0, column=0, padx=10, pady=10)

# Botão
botao = Button(janela, command=executar, width=8, height=1, text="Clique aqui", relief="sunken", fg='#fcb603', bg='black')
botao.grid(row=0, column=1, padx=10, pady=10)



janela.mainloop()