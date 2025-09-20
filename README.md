# Simulador de Navegação Anônima (Projeto)

> Aplicação web educativa que simula uma experiência de navegação “anônima” e um fórum anônimo. Feita para fins acadêmicos e demonstrativos — **não** acessa a real dark web nem contém links maliciosos.

---

## Sobre o projeto
Este projeto é uma página web que simula, de forma segura e controlada, funcionalidades associadas a uma navegação “anônima” e a um fórum anônimo. O objetivo é demonstrar conceitos de autenticação, gerenciamento de sessão, criação/consumo de conteúdo e tratamento de uploads (simulados) em um ambiente de desenvolvimento.

### Principais conceitos demonstrados:
- CRUD de usuários (registro, atualização de senha, exclusão)
- Autenticação (login/logoff)
- Modo “anônimo” temporário (usuário anônimo gerado para a sessão)
- Interface de busca (redirecionamento para mecanismos de busca reais)
- Fórum anônimo: criar post, visualizar posts, recarregar (atualizar visualizações), excluir posts
- Uploads de imagem para análise (armazenamento seguro como arquivo/URL — simulado)

> Obs: Tudo é simulado para fins pedagógicos. O sistema **não** redireciona para conteúdos ilegais nem executa código malicioso.

---

## Demonstração
Insira aqui screenshots/GIFs do projeto (frontend). Exemplo:

---

## Funcionalidades

- **Autenticação**
  - Registro de novo usuário
  - Login / Logout
  - Atualização de senha
  - Exclusão de conta

- **Modo Anônimo**
  - Gera um usuário temporário que existe apenas enquanto a sessão anônima estiver ativa
  - Requer que o usuário esteja deslogado para ativar

- **Busca**
  - Caixa de busca que redireciona consultas para um mecanismo de busca (ex.: Google)
  - Botões de ação e navegação (apenas UI / links seguros)

- **Fórum Anônimo**
  - Criar post anônimo
  - Visualizar posts
  - Recarregar posts (simula atualização de visualizações)
  - Excluir todos os posts (ação administrativa disponível na UI de desenvolvimento)

- **Uploads (simulados)**
  - Usuário pode enviar imagem para “análise”; imagens são armazenadas localmente/temporariamente e referenciadas no histórico do chat/forum (nenhuma análise externa é feita por padrão)
