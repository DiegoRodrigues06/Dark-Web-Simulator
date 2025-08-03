# login.py

import tkinter as tk
from tkinter import messagebox
import app_state
from gui.tela_att_senha import TelaAttSenha
from gui.tela_del_conta import TelaDeletarConta
from gui.tela_nav import abrir_navegador
from gui.tela_cadastro import TelaCadastro
from login import autenticar_usuario

class TelaLogin:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Usuário").grid(row=0, column=0)
        tk.Label(self.frame, text="Senha").grid(row=1, column=0)

        self.entry_user = tk.Entry(self.frame)
        self.entry_pass = tk.Entry(self.frame, show="*")
        self.entry_user.grid(row=0, column=1)
        self.entry_pass.grid(row=1, column=1)

        tk.Button(self.frame, text="Entrar", command=self.login).grid(row=2, columnspan=2, pady=10)

        tk.Button(self.frame, text="Cadastrar-se", command=self.cadastrar).grid(row=3, columnspan=2, pady=10)

        tk.Button(self.frame, text="Esqueceu a senha?", command=self.atualizar_senha).grid(row=4, columnspan=2, pady=10)

        tk.Button(self.frame, text="excluir conta", command=self.deletar_conta).grid(row=5, columnspan=2, pady=10)

    def login(self):
        nome = self.entry_user.get()
        senha = self.entry_pass.get()

        if nome and senha:
            sucesso = autenticar_usuario(nome, senha)
            if sucesso:
                app_state.usuario_logado = True
                app_state.usuario_nome = nome
                self.frame.destroy()
                abrir_navegador(self.master)
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos.")
        else:
            messagebox.showwarning("Erro", "Preencha usuário e senha.")

    def cadastrar(self):
        self.frame.destroy()
        TelaCadastro(self.master)

    def atualizar_senha(self):
        self.frame.destroy()
        TelaAttSenha(self.master)

    def deletar_conta(self):
        self.frame.destroy()
        TelaDeletarConta(self.master)
