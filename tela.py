import tkinter as tk
class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("500x400")
        self.janela.title("Votação")


app = tk.Tk()
Tela(app)
app.mainloop()
