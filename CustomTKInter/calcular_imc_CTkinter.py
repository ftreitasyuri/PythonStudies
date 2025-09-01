import customtkinter as ctk

# Lista cores
cores = [
    "#2C3E50",
    '#ECF0F1',
    '#3498DB',
    '#16A085',
    '#95A5A6'
]

janela = ctk.CTk()
janela.title("Calculadora de IMC")
janela.geometry('440x520')
janela.configure(fg_color=cores[1])

# Dividindo a janela
quadro_superior = ctk.CTkFrame(janela, width=400, height=90, corner_radius=15)
# Posicionando frame na janela
quadro_superior.grid(row=0, column=0, sticky='nsew',padx=20, pady=20)


quadro_inferior = ctk.CTkFrame(janela, width=400, height=350, corner_radius=15)
# Posicionando frame na janela
quadro_inferior.grid(row=1, column=0, sticky='nsew',padx=20, pady=20)

# Configuar o quadro superior
nome_app = ctk.CTkLabel(quadro_superior, height=70,
                        text='Calculadora de IMC', 
                        font=('Helvetica', 30, 'bold'),
                        text_color=cores[3],
                        anchor="center"
                        )
# nome_app.grid(row=0, column=0, padx=10, pady=10)
nome_app.place(x=60, y=15)

# Função para calular IMG

def calcular():
    #degub
    # print('Funcionou')
    
    peso = float(e_peso.get())
    altura = float(e_altura.get())
    
    resultado = peso / (altura ** 2)
    
    if resultado < 16.6:
        l_descricao.configure(text='Seu IMC é : Abaixo do peso')
    elif resultado >= 18.5 and resultado < 24.9:
        l_descricao.configure(text='Seu IMC é: Normal')
    elif resultado >= 25 and resultado < 29.9:
        l_descricao.configure(text='Seu IMC é: Sobrepeso')
    else:
        l_descricao.configure(text='Seu IMC é: Obesidade')
        
    l_resultado.configure(text='{:.{}f}'.format(resultado,2))

# Configurar o quadro inferior
l_peso = ctk.CTkLabel(quadro_inferior, text='Digite seu peso (Kg)',
                      text_color=cores[0],
                      font=('Helvetica', 14),
                      
                      )
l_peso.grid(row=0, column=0, sticky='nw', padx=15, pady=15)

e_peso = ctk.CTkEntry(quadro_inferior, width=180,
                      font=('Helvetica', 16),
                      justify='center',
                      corner_radius=12
                      )
e_peso.grid(row=0, column=1, sticky='nsew', padx=15, pady=15)


# Altura
l_altura = ctk.CTkLabel(quadro_inferior, text='Digite sua altura (Cm)',
                      text_color=cores[0],
                      font=('Helvetica', 14),
                      
                      )
l_altura.grid(row=1, column=0, sticky='nw', padx=15, pady=15)

e_altura = ctk.CTkEntry(quadro_inferior, width=180,
                      font=('Helvetica', 16),
                      justify='center',
                      corner_radius=12
                      )
e_altura.grid(row=1, column=1, sticky='nsew', padx=15, pady=15)

# Resultado
l_resultado = ctk.CTkLabel(quadro_inferior, text='---', width=5,
                           height=1,
                            text_color=cores[0],
                            font=('Helvetica', 32, 'bold'),
                            anchor='center',
                            corner_radius=12
                      
                      )
l_resultado.grid(row=2, column=1, columnspan=2, sticky='nw', padx=15, pady=30)


# Resultado descrição
l_descricao = ctk.CTkLabel(quadro_inferior, text='',
                            text_color=cores[0],
                            font=('Helvetica', 15),
                            # anchor='center',
                            justify='center'                           
                      
                      )
l_descricao.grid(row=3, column=0, columnspan=2)
# l_descricao.grid(row=3, column=0, padx=15, pady=15)

# Botão

b_calcular = ctk.CTkButton(quadro_inferior,
                           text='Calcular',
                           width=180, height=50,
                           font=('Helvetica', 16, 'bold'),
                           fg_color=cores[2],
                           hover_color=cores[4],
                           corner_radius=12,
                           command=calcular
                           )
b_calcular.grid(row=4, column=0, columnspan=2, padx=15, pady=25)


janela.mainloop()