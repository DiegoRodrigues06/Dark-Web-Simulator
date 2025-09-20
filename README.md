# Dark Web Simulator

## Sobre o projeto
Este projeto é uma página web que simula, de forma segura e controlada, funcionalidades associadas a uma navegação “anônima” e a um fórum anônimo. O objetivo é demonstrar conceitos de autenticação, gerenciamento de sessão, criação/consumo de conteúdo e tratamento de uploads (simulados).

### Principais conceitos demonstrados:
- CRUD de usuários (registro, atualização de senha, exclusão)
- Autenticação (login/logoff)
- Modo “anônimo” temporário (usuário anônimo gerado para a sessão)
- Interface de busca (redirecionamento para mecanismos de busca reais)
- Fórum anônimo: criar post, visualizar posts, recarregar (atualizar visualizações), excluir posts
- Uploads de imagem para análise (armazenamento seguro como arquivo/URL — simulado)

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
