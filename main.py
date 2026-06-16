"""
.\venv\Scripts\Activate.ps1 ---> para ativar o ambiente virtual
uvicorn main:app --reload ---> para rodar a aplicação

ruff check . --fix ---> para corrigir os erros de linting
black . ---> para formatar o código
"""

from fastapi import FastAPI, Depends, status

from sqlmodel import SQLModel, Session

from database import engine, get_session

from models.livro import Livro
from schemas.livro import LivroCreate

app = FastAPI()


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}


@app.post(
    "/livros",
    response_model=Livro,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar livro",
    description="Cadastra um novo livro na lista de leitura do usuário.",
    tags=["Livros"],
)
def criar_livro(livro: LivroCreate, session: Session = Depends(get_session)):
    novo_livro = Livro(**livro.model_dump())

    session.add(novo_livro)

    session.commit()

    session.refresh(novo_livro)

    return novo_livro
