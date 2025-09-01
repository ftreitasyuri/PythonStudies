import customtkinter as ctk

def botao_clicado():
    print("Botão foi clicado!")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("550x350")
        self.title("Botões com CTTKinter")
        
        self.label = ctk.CTkLabel(self, text="Olá, bem vindo ao custom ctkinter")
        self.label.place(x=5, y=5)
        
        self.botao = ctk.CTkButton(self, text='Clique aqui',
                                   width=200,
                                   height=40,
                                   fg_color=('white', 'gray'),
                                   text_color=("black", "white"),
                                   corner_radius=10,
                                   font=('Arial', 25),
                                   command=botao_clicado
                                   )
        
    
        self.botao.place(x=10, y=50)

# 
app = App()
app.mainloop()
