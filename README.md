# My Book List API

## Visão geral

API de lista de leitura de livros criada com FastAPI e SQLModel. A aplicação permite cadastrar, listar, atualizar e excluir livros, além de adicionar e listar trechos relacionados a cada livro.

Ao cadastrar um livro, a aplicação tenta buscar automaticamente a capa pelo Open Library.

## Pré-requisitos

- Python 3.11 ou superior
- Ambiente virtual Python configurado
- Dependências instaladas via `requirements.txt`

## Instalação

1. Crie um ambiente virtual:
   - `python -m venv .venv`
2. Ative o ambiente virtual:
   - PowerShell: `.venv\Scripts\Activate.ps1`
   - CMD: `.venv\Scripts\activate`
3. Instale as dependências:
   - `pip install -r requirements.txt`

## Executando o projeto

1. Abra um terminal na pasta do projeto.
2. Ative o ambiente virtual.
3. Execute:
   - `uvicorn main:app --reload`
4. Acesse a API em:
   - `http://127.0.0.1:8000`

## Documentação

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Banco de dados

- O projeto usa SQLite em `database.db`.
- As tabelas são criadas automaticamente quando a aplicação inicia.
- Caso o arquivo `database.db` não exista, ele será gerado na primeira execução.

## Endpoints

### Livros

- `POST /livros`
  - Cadastra um novo livro.

- `GET /livros`
  - Lista todos os livros.
  - Aceita filtro opcional por `status`.

- `PUT /livros/{livro_id}`
  - Atualiza os dados de um livro existente.

- `DELETE /livros/{livro_id}`
  - Exclui um livro.

### Trechos

- `POST /livros/{livro_id}/trechos`
  - Adiciona um trecho a um livro.

- `GET /livros/{livro_id}/trechos`
  - Lista os trechos de um livro.

- `DELETE /trechos/{trecho_id}`
  - Exclui um trecho.

## Tecnologias utilizadas

- Python 3.11
- FastAPI
- SQLModel
- Uvicorn
- Requests

## Comandos úteis

- `pip install -r requirements.txt` — instala as dependências do projeto
- `uvicorn main:app --reload` — inicia a API em modo de desenvolvimento
- `pip freeze > requirements.txt` — atualiza o arquivo com as dependências instaladas
- `ruff check . --fix` — verifica e corrige problemas de lint no código
- `black .` — formata o código automaticamente

## Observações

- Se desejar, adicione `database.db` ao `.gitignore` para evitar versionar o banco local.
