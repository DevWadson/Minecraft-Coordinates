""" . """
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from src.database.SQL.base import Base

class Local(Base):
    """Classe que representa o local que a coordenada aponta (nome da coordenada)"""
    __tablename__ = "local"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_server = Column(Integer, ForeignKey("servidor.id"))
    id_dim = Column(Integer, ForeignKey("dimensao.id"))
    nome = Column(VARCHAR(50), nullable=False)

    #Seleciona as dimensões do local
    #Seleciona as coordenadas do local
    dimension = relationship("Dimensao", back_populates="local_name")
    coord = relationship("Coordenada", back_populates="local")
