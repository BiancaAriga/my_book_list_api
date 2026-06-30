from typing import Optional

from sqlmodel import SQLModel, Relationship, Field
from models.livro import Livro


class Trecho(SQLModel, table=True):
    __tablename__ = "trechos"

    id: Optional[int] = Field(default=None, primary_key=True)

    texto: str

    livro_id: int = Field(foreign_key="livros.id")

    livro: "Livro" = Relationship(back_populates="trechos")
