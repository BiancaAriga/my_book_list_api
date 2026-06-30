from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Relationship, Field
from enum import Enum

from models.trecho import Trecho


class LivroStatus(str, Enum):
    QUERO_LER = "Quero Ler"
    LENDO = "Lendo"
    FINALIZADO = "Finalizado"
    ABANDONADO = "Abandonado"


class Livro(SQLModel, table=True):
    __tablename__ = "livros"

    id: Optional[int] = Field(default=None, primary_key=True)

    nome: str

    autor: str

    categoria: Optional[str] = None

    rating: Optional[int] = Field(default=None, ge=1, le=5)

    data_inicio: Optional[date] = None

    data_fim: Optional[date] = None

    status: LivroStatus = LivroStatus.QUERO_LER

    trechos: list["Trecho"] = Relationship(back_populates="livro", cascade_delete=True)
