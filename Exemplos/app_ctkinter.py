import customtkinter as ctk
# Função converte_texto recebe dois parametros opc e texto
from conversor_texto import converte_texto


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

        self.geometry("500x350")
        self.title("App de teste")
        self.configure(fg_color=self.cores[1])
         
        self.criar_widgets()
        
    def criar_widgets(self):
        
        # Dividindo janela com frames
        self.quadro_superior = ctk.CTkFrame(self, width=450, height=90, corner_radius=15)
        self.quadro_superior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

        
        
        self.quadro_inferior = ctk.CTkFrame(self, width=400, height=350, corner_radius=15)
        self.quadro_inferior.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)
        # self.quadro_superior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        
        # Configuração quadro superior
        self.nome_app = ctk.CTkLabel(self.quadro_superior, height=70,
            text='Conversor de Texto', 
            font=('Helvetica', 30, 'bold'),
            text_color=self.cores[3],
            anchor="center")
        self.nome_app.place(x=60, y=15)
        
        # Label
        self.label = ctk.CTkLabel(self.quadro_inferior, text='Selecione o valor que deseja operar', width=40, height=28, fg_color='transparent')
        self.label.grid(row=1, column=0, sticky='nw', padx=15, pady=15)
        
        self.opcoes = ctk.CTkComboBox(self.quadro_inferior, values=["1", "2"],
                                    
                                    )
        self.opcoes.grid(row=1, column=0, sticky='nw', padx=15, pady=15)

    
        # Entry
        self.e_opcao = ctk.CTkEntry(self.quadro_inferior, 
                                    width=180,
                                    justify='center'
                                    )
        self.e_opcao.grid(row=1, column=1, sticky='nw', padx=15, pady=15)
    
        
        # self.label = ctk.CTkLabel(self.quadro_inferior, text='Digite o texto que deseja converte', width=40, height=28, fg_color='transparent')
        # self.label.grid(row=1, column=0, sticky='nw', padx=15, pady=15)
        
app = App()
app.mainloop()
