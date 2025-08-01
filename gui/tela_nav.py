# navegador.py

import tkinter as tk
from tkinter import messagebox
import webbrowser
import random
import app_state

def abrir_navegador(master):
    frame = tk.Frame(master)
    frame.pack(padx=20, pady=20)

    label_user = tk.Label(frame, text=f"Usuário: {app_state.usuario_nome}")
    label_user.pack()

    # Campo de busca
    entry_busca = tk.Entry(frame, width=40)
    entry_busca.pack()

    def pesquisar():
        if app_state.modo_anonimo:
            messagebox.showwarning("Restrito", "Anon não pode usar o GuluGulu.")
        else:
            termo = entry_busca.get()
            if termo:
                webbrowser.open(f"https://www.google.com/search?q={termo}")
            else:
                messagebox.showinfo("Busca", "Digite algo para pesquisar.")

    btn_buscar = tk.Button(frame, text="Pesquisar no GuluGulu", command=pesquisar)
    btn_buscar.pack(pady=5)

    # VPN toggle
    def ativar_vpn():
        app_state.vpn_ativa = True
        label_vpn.config(text="VPN Ativa - Localização: Sudão do Sul 🇸🇸")

    label_vpn = tk.Label(frame, text="VPN Desativada")
    label_vpn.pack()

    tk.Button(frame, text="Ativar VPN", command=ativar_vpn).pack(pady=5)

    # Entrar na deep web
    def entrar_deepweb():
        if not app_state.vpn_ativa:
            messagebox.showwarning("VPN", "Ative a VPN primeiro.")
            return

        if app_state.usuario_logado:
            app_state.usuario_logado = False
            app_state.usuario_nome = ""
            app_state.modo_anonimo = True
            app_state.anon_user = f"anon{random.randint(100,999)}"
            label_user.config(text=f"Usuário: {app_state.anon_user}")
            label_ocultos.pack()
            for link in links_ocultos:
                link.pack()
            btn_buscar.config(state="disabled")
            entry_busca.config(state="disabled")

    tk.Button(frame, text="Entrar na Deep Web", command=entrar_deepweb).pack(pady=10)

    label_ocultos = tk.Label(frame, text="🌑 Links ocultos liberados:", fg="red")
    label_ocultos.pack_forget()

    links_ocultos = []
    for texto, url in [
        ("Comprar dados vazados", "https://example.com/dados"),
        ("Fórum de hackers", "https://example.com/forum"),
        ("Baixar malware", "https://example.com/malware")
    ]:
        link = tk.Label(frame, text=texto, fg="blue", cursor="hand2")
        link.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
        link.pack_forget()
        links_ocultos.append(link)
