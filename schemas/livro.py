from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field

from models.livro import LivroStatus


class LivroCreate(SQLModel):
    nome: str
    autor: str
    categoria: Optional[str] = None
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    status: Optional[LivroStatus] = None


class LivroUpdate(SQLModel):
    nome: Optional[str] = None
    autor: Optional[str] = None
    categoria: Optional[str] = None
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    status: Optional[LivroStatus] = None
