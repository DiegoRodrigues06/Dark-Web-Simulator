# login.py

import tkinter as tk
from tkinter import messagebox
import app_state
from gui.tela_nav import abrir_navegador

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

    def login(self):
        user = self.entry_user.get()
        password = self.entry_pass.get()

        if user and password:
            app_state.usuario_logado = True
            app_state.usuario_nome = user
            self.frame.destroy()
            abrir_navegador(self.master)
        else:
            messagebox.showwarning("Erro", "Preencha usuário e senha.")
