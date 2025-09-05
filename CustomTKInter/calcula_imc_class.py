import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Lista de cores
        self.cores = [
            "#2C3E50",
            '#ECF0F1',
            '#3498DB',
            '#16A085',
            '#95A5A6'
        ]

        self.title("Calculadora de IMC")
        self.geometry('440x520')
        self.configure(fg_color=self.cores[1])
        
        self.criar_widgets()

    def criar_widgets(self):
        # Dividindo a janela
        self.quadro_superior = ctk.CTkFrame(self, width=400, height=90, corner_radius=15)
        self.quadro_superior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

        self.quadro_inferior = ctk.CTkFrame(self, width=400, height=350, corner_radius=15)
        self.quadro_inferior.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

        # Configurar o quadro superior
        self.nome_app = ctk.CTkLabel(self.quadro_superior, height=70,
                                     text='Calculadora de IMC', 
                                     font=('Helvetica', 30, 'bold'),
                                     text_color=self.cores[3],
                                     anchor="center")
        self.nome_app.place(x=60, y=15)

        # Configurar o quadro inferior
        self.l_peso = ctk.CTkLabel(self.quadro_inferior, text='Digite seu peso (Kg)',
                                   text_color=self.cores[0],
                                   font=('Helvetica', 14))
        self.l_peso.grid(row=0, column=0, sticky='nw', padx=15, pady=15)

        self.e_peso = ctk.CTkEntry(self.quadro_inferior, width=180,
                                   font=('Helvetica', 16),
                                   justify='center',
                                   corner_radius=12)
        self.e_peso.grid(row=0, column=1, sticky='nsew', padx=15, pady=15)

        self.l_altura = ctk.CTkLabel(self.quadro_inferior, text='Digite sua altura (Cm)',
                                     text_color=self.cores[0],
                                     font=('Helvetica', 14))
        self.l_altura.grid(row=1, column=0, sticky='nw', padx=15, pady=15)
        
        
        
        

        self.e_altura = ctk.CTkEntry(self.quadro_inferior, width=180,
                                     font=('Helvetica', 16),
                                     justify='center',
                                     corner_radius=12)
        self.e_altura.grid(row=1, column=1, sticky='nsew', padx=15, pady=15)

        self.l_resultado = ctk.CTkLabel(self.quadro_inferior, text='---', width=5,
                                        height=1,
                                        text_color=self.cores[0],
                                        font=('Helvetica', 32, 'bold'),
                                        anchor='center',
                                        corner_radius=12)
        self.l_resultado.grid(row=2, column=1, columnspan=2, sticky='nw', padx=15, pady=30)

        self.l_descricao = ctk.CTkLabel(self.quadro_inferior, text='',
                                        text_color=self.cores[0],
                                        font=('Helvetica', 15),
                                        justify='center')
        self.l_descricao.grid(row=3, column=0, columnspan=2)

        self.b_calcular = ctk.CTkButton(self.quadro_inferior,
                                        text='Calcular',
                                        width=180, height=50,
                                        font=('Helvetica', 16, 'bold'),
                                        fg_color=self.cores[2],
                                        hover_color=self.cores[4],
                                        corner_radius=12,
                                        command=self.calcular)
        self.b_calcular.grid(row=4, column=0, columnspan=2, padx=15, pady=25)

    def calcular(self):
        try:
            peso = float(self.e_peso.get())
            altura = float(self.e_altura.get())
            
            # Converte a altura de cm para metros
            altura_m = altura / 100
            
            resultado = peso / (altura_m ** 2)
            
            self.l_resultado.configure(text='{:.{}f}'.format(resultado, 2))

            if resultado < 18.5:
                self.l_descricao.configure(text='Abaixo do peso')
            elif resultado >= 18.5 and resultado < 24.9:
                self.l_descricao.configure(text='Peso ideal (Normal)')
            elif resultado >= 25 and resultado < 29.9:
                self.l_descricao.configure(text='Sobrepeso')
            elif resultado >= 30 and resultado < 39.9:
                self.l_descricao.configure(text='Obesidade')
            else:
                self.l_descricao.configure(text='Obesidade grave')
        except ValueError:
            self.l_descricao.configure(text='Por favor, digite valores válidos.')

if __name__ == "__main__":
    app = App()
    app.mainloop()
