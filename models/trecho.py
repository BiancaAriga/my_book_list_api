from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.livro import Livro


class Trecho(SQLModel, table=True):
    __tablename__ = "trechos"

    id: Optional[int] = Field(default=None, primary_key=True)

    texto: str

    livro_id: int = Field(foreign_key="livros.id")

    livro: Optional["Livro"] = Relationship(back_populates="trechos")
