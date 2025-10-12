""" . """
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from src.database.SQL.base import Base

class Dimensao(Base):
    """Classe que representa a dimensão que o personagem está"""
    __tablename__ = "dimensao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_server = Column(Integer, ForeignKey("servidor.id"))
    nome = Column(VARCHAR(40))
