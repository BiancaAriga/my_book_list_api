from sqlmodel import SQLModel


class TrechoCreate(SQLModel):
    texto: str
