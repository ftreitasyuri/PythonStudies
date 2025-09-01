import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("550x350")
        self.title("Labels em CTTKinter")
        
        self.label = ctk.CTkLabel(self, text="Olá, bem vindo ao custom ctkinter")
        self.label.place(x=5, y=5)

        self.nome = ctk.CTkEntry(self, placeholder_text='Digite seu nome',
                                 width=250,
                                 height=40,
                                 fg_color=('white', 'gray'),
                                 text_color=('gray', 'green'),
                                 corner_radius=40,
                                 font=('Arial', 25)
                                 )
        def mostrar():
            nome_entry = self.nome.get()
            print(nome_entry)
        self.nome.place(relx=0.5, rely=0.5, anchor='center')
        
        self.botao = ctk.CTkButton(self, text="Mostrar Nome", command=mostrar)
        self.botao.place(relx=0.5, rely=0.7, anchor='center')
# 
app = App()
app.mainloop()
