import tkinter as tk
from tkinter import messagebox
import login  


class TelaAttSenha:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Usuario").grid(row=0, column=0)
        tk.Label(self.frame, text="Nova senha").grid(row=1, column=0)
        tk.Label(self.frame, text="Confirmação").grid(row=2, column=0)

        self.entry_usuario = tk.Entry(self.frame)
        self.entry_senha = tk.Entry(self.frame, show="*")
        self.entry_confirma = tk.Entry(self.frame, show="*")
        self.entry_usuario.grid(row=0, column=1)
        self.entry_senha.grid(row=1, column=1)
        self.entry_confirma.grid(row=2, column=1)

        tk.Button(self.frame, text="Atualizar", command=self.atualizar).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame, text="Voltar", command=self.voltar).grid(row=4, columnspan=2)

    def atualizar(self):
        nome= self.entry_usuario.get()
        senha = self.entry_senha.get()
        confirma = self.entry_confirma.get()

        if senha and confirma:
            if senha == confirma:
                login.atualizar_senha(nome, senha)
                messagebox.showinfo("Sucesso", "Senha atualizada com sucesso!")
                self.voltar()
            else:
                messagebox.showerror("Erro", "As senhas não coincidem.")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def voltar(self):
        from gui.tela_login import TelaLogin 
        self.frame.destroy()
        TelaLogin(self.master)
