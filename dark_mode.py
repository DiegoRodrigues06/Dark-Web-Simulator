import random

def criar_perfil_anonimo():
    nomes = ["anon", "ghost", "darkwolf", "rootx"]
    numero = random.randint(100, 999)
    return f"{random.choice(nomes)}{numero}"

# Os posts só ficam em RAM
posts = []

def postar_crime(autor, conteudo):
    posts.append((autor, conteudo))

def listar_crimes():
    return posts
