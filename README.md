# my_book_list_api

## Visão geral

Este projeto é uma API simples de lista de leitura de livros construída com FastAPI e SQLModel. A API permite cadastrar, listar, atualizar e deletar livros, além de expor a documentação automática em um navegador.

## Pré-requisitos

- Python 3.11 ou superior
- Ambiente virtual Python configurado
- Dependências instaladas via `requirements.txt`

## Como rodar o projeto

1. Abra um terminal na pasta do projeto.
2. Ative o ambiente virtual:
   - Windows PowerShell: `.\venv\Scripts\Activate.ps1`
3. Inicie a aplicação:
   - `uvicorn main:app --reload`
4. A API estará disponível em `http://127.0.0.1:8000`

## Como acessar a documentação

Após iniciar a aplicação, use um navegador para acessar:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Comandos úteis

- `ruff check . --fix` ---> para corrigir os erros de linting
- `black .` ---> para formatar o código

## Endpoints principais

- `POST /livros` ---> cadastrar um novo livro
- `GET /livros/` ---> listar todos os livros
- `GET /livros/{livro_id}` ---> obter um livro pelo ID
- `PUT /livros/{livro_id}` ---> atualizar um livro existente
- `DELETE /livros/{livro_id}` ---> deletar um livro

