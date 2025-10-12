""" . """
from sqlalchemy import Column, Integer, Float, ForeignKey
from src.database.SQL.base import Base

class Coordenada(Base):
    """Tabela que indica a posição geográfica do personagem"""
    __tablename__ = "coordenada"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_server = Column(Integer, ForeignKey("servidor.id"))
    id_dim = Column(Integer, ForeignKey("dimensao.id"))
    id_local = Column(Integer, ForeignKey("local.id"))
    x = Column("x", Float, nullable=False)
    y = Column("y", Float, nullable=False)
    z = Column("z", Float, nullable=False)
