import tkinter as tk
from tkinter import messagebox
import banco_de_dados as bd
class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("500x400")
        self.janela.title("Votação")

        # Login/Cadastro
        self.frm_login = tk.Frame(self.janela)
        self.frm_login.pack(pady=50)

        self.lbl_user = tk.Label(self.frm_login, text="Usuário")
        self.lbl_user.grid(column=0, row=0)
        self.ent_user = tk.Entry(self.frm_login)
        self.ent_user.grid(column=0, row=1)

        self.lbl_null = tk.Label(self.frm_login)
        self.lbl_null.grid(column=0, row=2)

        self.lbl_senha = tk.Label(self.frm_login, text="Senha")
        self.lbl_senha.grid(column=0, row=3)
        self.ent_senha = tk.Entry(self.frm_login, show="*")
        self.ent_senha.grid(column=0, row=4)

        self.lbl_null1 = tk.Label(self.frm_login)
        self.lbl_null1.grid(column=0, row=5)

        self.btn_login = tk.Button(self.frm_login, text="Entrar", command=self.login)
        self.btn_login.grid(column=0, row=6, columnspan=1)

        self.btn_cadastro = tk.Button(self.frm_login, text="Cadastre-se", command=self.cadastro)
        self.btn_cadastro.grid(column=0, row=7, pady=20)

        # Funções
    def login(self):
        user = self.ent_user.get()
        senha = self.ent_senha.get()
        if user == "":
            messagebox.showinfo("Insira um nome", "O campo nome está vazio!")
        elif senha == "":
            messagebox.showinfo("Insira um nome de usuário", "O campo nome de usuário está vazio!")
        else:
            query = 'SELECT user_name, senha FROM usuario;'
            valores = bd.consultar(query)
            logado = False
            for i in valores:
                if i[0] == user and i[1] == senha:
                    logado = True
            if logado:
                messagebox.showinfo("Logado", "Logado com sucesso!!!")
            else:
                messagebox.showinfo("Dados incorretos", "Usuário ou senha incorreto(s)")

    def cadastro(self):
        self.cadastro = tk.Toplevel()
        self.cadastro.geometry("300x200")
        self.lbl_nome = tk.Label(self.cadastro, text="Nome")
        self.lbl_nome.pack()
        self.ent_nome = tk.Entry(self.cadastro)
        self.ent_nome.pack()

        self.lbl_user = tk.Label(self.cadastro, text="Nome de Usuário")
        self.lbl_user.pack()
        self.ent_user = tk.Entry(self.cadastro)
        self.ent_user.pack()

        self.lbl_senha = tk.Label(self.cadastro, text="Senha")
        self.lbl_senha.pack()
        self.ent_senha = tk.Entry(self.cadastro, show="*")
        self.ent_senha.pack()

        self.btn_con_cadastro = tk.Button(self.cadastro, text="Confirmar", command=self.confirma_cadastro)
        self.btn_con_cadastro.pack()

    def confirma_cadastro(self):
        nome = self.ent_nome.get()
        user = self.ent_user.get()
        senha = self.ent_senha.get()
        if nome == "":
            messagebox.showinfo("Insira um nome", "O campo nome está vazio!")
        elif user == "":
            messagebox.showinfo("Insira um nome de usuário", "O campo nome de usuário está vazio!")
        elif senha == "":
            messagebox.showinfo("Insira uma senha", "O campo senha está vazio!")
        else:
            query = 'SELECT user_name FROM usuario;'
            valores = bd.consultar(query)
            confirmar = False
            for i in valores:
                if user == i:
                    confirmar = True
            if confirmar:
                query = f'INSERT INTO usuario ("nome", "user_name", "senha", "tipo", "status") VALUES ("{nome}", "{user}", "{senha}", "Usuário", 0);'
                bd.inserir(query)
                messagebox.showinfo("SUCESSO!", "Usuário criado com sucesso!")
                self.cadastro.destroy()
            else:
                messagebox.showinfo("Nome de usuário existente", "Nome de usuário já existente!")

app = tk.Tk()
Tela(app)
app.mainloop()
