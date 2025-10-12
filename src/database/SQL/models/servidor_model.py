""" . """
from sqlalchemy import Column, Integer, VARCHAR
from src.database.SQL.base import Base

class Servidor(Base):
    """Tabela que representa o mundo/servidor criado"""
    __tablename__ = "servidor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(VARCHAR(120), nullable=False)
