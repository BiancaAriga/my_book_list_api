from typing import Annotated

from fastapi import FastAPI, Depends, status, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import SQLModel, Session, select

from database import engine, get_session

from models.livro import Livro, LivroStatus
from schemas.livro import LivroCreate, LivroUpdate
from services.open_library import buscar_capa_livro

from models.trecho import Trecho
from schemas.trecho import TrechoCreate

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
    capa = buscar_capa_livro(livro.nome, livro.autor)

    novo_livro = Livro(**livro.model_dump(), imagem_url=capa)

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
    description="Lista todos os livros da lista de leitura do usuário. Opcionalmente, permite filtrar os resultados por status.",
    tags=["Livros"],
)
def ler_livros(
    session: SessionDep,
    status: LivroStatus | None = None,
) -> list[Livro]:
    consulta = select(Livro)

    if status is not None:
        consulta = consulta.where(Livro.status == status)

    return session.exec(consulta).all()


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


@app.post(
    "/livros/{livro_id}/trechos",
    response_model=Trecho,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar trecho",
    description="Cadastra um novo trecho na lista de leitura do usuário.",
    tags=["Trechos"],
)
def criar_trecho(livro_id: int, trecho: TrechoCreate, session: SessionDep) -> Trecho:
    livro = session.get(Livro, livro_id)

    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    novo_trecho = Trecho(**trecho.model_dump(), livro_id=livro_id)

    session.add(novo_trecho)

    session.commit()

    session.refresh(novo_trecho)

    return novo_trecho


@app.get(
    "/livros/{livro_id}/trechos",
    response_model=list[Trecho],
    summary="Listar trechos",
    description="Lista todos os trechos de um livro específico.",
    tags=["Trechos"],
)
def ler_trechos(
    livro_id: int,
    session: SessionDep,
) -> list[Trecho]:
    livro = session.get(Livro, livro_id)

    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    return livro.trechos


@app.delete(
    "/trechos/{trecho_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar trecho",
    description="Deleta um trecho do livro do usuário.",
    tags=["Trechos"],
)
def deletar_trecho(trecho_id: int, session: SessionDep):
    trecho = session.get(Trecho, trecho_id)

    if not trecho:
        raise HTTPException(status_code=404, detail="Trecho não encontrado")

    session.delete(trecho)
    session.commit()
