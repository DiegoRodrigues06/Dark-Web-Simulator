# eu devia ter feito essa parte do codigo junto com com o db.py
# mas agora é tarde demais, ja ta feito 🥸

from db import conectar
from db import criar_tabelas

criar_tabelas()

def cadastrar_usuario(nome, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
    conn.commit()
    conn.close()

def autenticar_usuario(nome, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def atualizar_senha(nome, nova_senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET senha = ? WHERE nome = ?", (nova_senha, nome))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0  

def deletar_usuario(nome, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

# PRIMEIRO CRUD CONCLUIDO 👆 !!!
