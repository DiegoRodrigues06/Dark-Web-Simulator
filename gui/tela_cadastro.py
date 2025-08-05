import tkinter as tk
from tkinter import messagebox
import login as login 

class TelaCadastro:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Novo usuário").grid(row=0, column=0)
        tk.Label(self.frame, text="Nova senha").grid(row=1, column=0)

        self.entry_user = tk.Entry(self.frame)
        self.entry_pass = tk.Entry(self.frame, show="*")
        self.entry_user.grid(row=0, column=1)
        self.entry_pass.grid(row=1, column=1)

        tk.Button(self.frame, text="Cadastrar", command=self.cadastrar).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.frame, text="Voltar", command=self.voltar).grid(row=3, columnspan=2)

    def cadastrar(self):
        nome = self.entry_user.get()
        senha = self.entry_pass.get()

        if nome and senha:
            login.autenticar_usuario(nome, senha)
            sucesso = login.cadastrar_usuario(nome, senha)
            if not sucesso:
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                self.voltar()
            else:
                messagebox.showerror("Erro", "Usuário já existe.")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def voltar(self):
        from gui.tela_login import TelaLogin  
        self.frame.destroy()
        TelaLogin(self.master)
