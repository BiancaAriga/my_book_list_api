from typing import Annotated

from fastapi import FastAPI, Depends, status, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import SQLModel, Session, select

from database import engine, get_session

from models.livro import Livro
from schemas.livro import LivroCreate, LivroUpdate

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://127.0.0.1:5501",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.post(
    "/livros",
    response_model=Livro,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar livro",
    description="Cadastra um novo livro na lista de leitura do usuário.",
    tags=["Livros"],
)
def criar_livro(livro: LivroCreate, session: SessionDep) -> Livro:
    novo_livro = Livro(**livro.model_dump())

    session.add(novo_livro)

    session.commit()

    session.refresh(novo_livro)

    return novo_livro


@app.delete(
    "/livros/{livro_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar livro",
    description="Deleta um livro da lista de leitura do usuário.",
    tags=["Livros"],
)
def deletar_livro(livro_id: int, session: SessionDep):
    livro = session.get(Livro, livro_id)

    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    session.delete(livro)
    session.commit()


@app.get(
    "/livros",
    response_model=list[Livro],
    summary="Listar livros",
    description="Lista todos os livros da lista de leitura do usuário.",
    tags=["Livros"],
)
def ler_livros(
    session: SessionDep,
) -> list[Livro]:
    return session.exec(select(Livro)).all()
    

@app.put(
    "/livros/{livro_id}",
    response_model=Livro,
    summary="Atualizar livro",
    description="Atualiza as informações de um livro específico da lista de leitura do usuário.",
    tags=["Livros"],
)
def atualizar_livro(
    livro_id: int,
    livro_update: LivroUpdate,
    session: SessionDep,
) -> Livro:
    livro = session.get(Livro, livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    for key, value in livro_update.model_dump(exclude_unset=True).items():
        setattr(livro, key, value)

    session.commit()
    session.refresh(livro)
    return livro
