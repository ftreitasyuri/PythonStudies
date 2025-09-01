import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("550x350")
        self.title("Labels em CTTKinter")
        
        self.label = customtkinter.CTkLabel(self, text="Olá, bem vindo ao custom ctkinter")
        self.label.place(x=5, y=5)

# 
app = App()
app.mainloop()
