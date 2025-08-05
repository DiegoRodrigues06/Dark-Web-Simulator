import tkinter as tk
from tkinter import messagebox
import webbrowser
import random
import app_state as app_state
import os
import dark_mode as dark_mode


base_dir = os.path.dirname(__file__)  # pega a pasta onde está o arquivo .py atual
caminho_script = os.path.join(base_dir, "..", "mene", "script.bat")
caminho_script = os.path.abspath(caminho_script) # transcreve pro seu diretorio


# --- FUNÇÃO PRIONCIPAL: abrir_navegador ---
def abrir_navegador(master):
    frame = tk.Frame(master)
    frame.pack(padx=20, pady=20)

    label_user = tk.Label(frame, text=f"Usuário: {app_state.usuario_nome or 'Deslogado'}")
    label_user.pack()

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


    # Ativar VPN
    def ativar_vpn():
        app_state.vpn_ativa = True
        label_vpn.config(text="VPN Ativa - Localização: Sudão do Sul 🇸🇸")

    label_vpn = tk.Label(frame, text="VPN Desativada")
    label_vpn.pack()

    tk.Button(frame, text="Ativar VPN", command=ativar_vpn).pack(pady=5)


    # Deslogar
    def deslogar(label_user):
        app_state.usuario_logado = False
        app_state.usuario_nome = ""
        label_user.config(text="Usuário: Deslogado")

    tk.Button(frame, text="Deslogar", fg="red", command=lambda: deslogar(label_user)).pack(pady=10)

    label_ocultos = tk.Label(frame, text="Você entrou na Deep Web👻:", fg="red")
    label_ocultos.pack_forget()


    # Links ocultos
    # criando uma lista para armazenar os links ocultos
    links_ocultos = []
    for texto, url in [
        ("Comprar dados vazados", "https://br.pinterest.com/pin/pode-no-man-em-2024--645492559121341138/"),
        ("Fique rico em um clique!", "https://youtu.be/dQw4w9WgXcQ?si=o68LO_MzKVyVRmwp"),
        ("Baixar malware (100% seguro)", caminho_script),
    ]:
        link = tk.Label(frame, text=texto, fg="blue", cursor="hand2")
        link.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
        link.pack_forget()
        links_ocultos.append(link)


    # Deep Web
    def entrar_deepweb():
        if not app_state.vpn_ativa or app_state.usuario_logado:
            messagebox.showwarning("Aviso ⚠️", "Para sua segurança, ative a VPN e deslogue da conta.")
            return

        app_state.modo_anonimo = True
        app_state.anon_user = f"anon{random.randint(100,999)}"
        label_user.config(text=f"Usuário: {app_state.anon_user}")
        label_ocultos.pack()
        for link in links_ocultos:
            link.pack()
        btn_buscar.config(state="disabled")
        entry_busca.config(state="disabled")
        tk.Button(frame, text="Postar conteúdo anônimo", command=postar_conteudo).pack(pady=5)
        tk.Button(frame, text="Ver conteúdos postados", command=ver_posts).pack(pady=5)
        tk.Button(frame, text="Excluir todos os posts ☠️", command=excluir_posts).pack(pady=5)

    tk.Button(frame, text="Entrar na Deep Web", command=entrar_deepweb).pack(pady=10)


    # Fazer posts anônimos
    def postar_conteudo():
        def enviar():
            texto = entrada.get("1.0", "end").strip()
            if texto:
                dark_mode.salvar_post(app_state.anon_user, texto)
                messagebox.showinfo("Sucesso", "Sua mensagem foi postada.")
                janela.destroy()

        janela = tk.Toplevel(master)
        janela.title("Fazer post anônimo")
        tk.Label(janela, text="O que você quer postar?").pack()
        entrada = tk.Text(janela, height=5, width=40)
        entrada.pack(pady=5)
        tk.Button(janela, text="Postar", command=enviar).pack()


    # Ver posts anônimos
    def ver_posts():
        posts = dark_mode.buscar_posts()
        if not posts:
            messagebox.showinfo("Nada aqui", "Nada foi postado ainda.")
            return

        janela = tk.Toplevel(master)
        janela.title("Posts Anônimos")

        for autor, conteudo, visualizado in posts:
            status = "👁️" if visualizado else "🆕"
            texto = f"{status} {autor}: {conteudo}"
            tk.Label(janela, text=texto, wraplength=400, justify="left").pack(anchor="w", padx=10, pady=2)

        def recarregar():
            dark_mode.marcar_todos_como_visualizados()
            janela.destroy()
            ver_posts()  # reabre a tela com posts atualizados

        
        tk.Button(janela, text="🔄 Recarregar (marcar como lido)", command=recarregar).pack(pady=10)


    # Excluir posts
    def excluir_posts():
        if messagebox.askyesno("Excluir todos os posts", "Você tem certeza que deseja excluir todos os posts?"):
            dark_mode.excluir_todos_posts()
            messagebox.showinfo("Sucesso", "Todos os posts foram excluídos.")


    # Voltar
    def voltar():
        from gui.tela_login import TelaLogin
        frame.destroy()
        TelaLogin(master)

    tk.Button(frame, text="voltar", command=voltar).pack(pady=5)
