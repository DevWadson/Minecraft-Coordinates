""" . """
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from src.database.SQL.base import Base

class Servidor(Base):
    """Tabela que representa o mundo/servidor criado"""
    __tablename__ = "servidor"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(VARCHAR(120), nullable=False)

    #Seleciona as dimensões do servidor
    dimension = relationship("Dimensao")
