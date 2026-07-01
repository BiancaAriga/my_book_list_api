from datetime import date
from typing import Optional, TYPE_CHECKING, List

from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

if TYPE_CHECKING:
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

    status: LivroStatus = Field(default=LivroStatus.QUERO_LER)

    imagem_url: str | None = None

    trechos: List["Trecho"] = Relationship(back_populates="livro", cascade_delete=True)
