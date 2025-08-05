# Nesse codigo, o banco de dados para o modo anonimo é criado. o usuario anonimo
# é gerado automaticamente na pagina "tela_nav.py" e aqui, é onde são gerenciados os 
# posts desses usuarios, aqui você pode gerar um post e vizualizar os posts feitos,
# quando a pagina é fechada, o usuario gerado vai pro limbo, e nunca mais pode ser 
# acessado novamente, e como eu to sem ideia, você vai ser o adiminastro supremo
# que pode deletar o post de todo mundo, e tambem aqui tem a função de atualizar
# o estado de visualização do post, POR QUE? porque eu to sem ideia, foi isso 
# que deu pra fazer kkkkkkkkk.
# aqui segundo crud concluido 🙏


import sqlite3

def conectar():
    return sqlite3.connect('bd/anon_posts.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts_anonimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        autor TEXT NOT NULL,
        conteudo TEXT NOT NULL,
        visualizado INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def salvar_post(autor, conteudo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts_anonimos (autor, conteudo) VALUES (?, ?)', (autor, conteudo))
    conn.commit()
    conn.close()

def buscar_posts():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT autor, conteudo, visualizado FROM posts_anonimos')
    dados = cursor.fetchall()
    conn.close()
    return dados

def excluir_todos_posts():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM posts_anonimos')
    conn.commit()
    conn.close()

def marcar_todos_como_visualizados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE posts_anonimos SET visualizado = 1 WHERE visualizado = 0")
    conn.commit()
    conn.close()

criar_tabela()

