"""ARQUIVO RESPONSÁVEL PELA CRIAÇÃO DO SQLITE DB."""
#Módulo retorna arquivo.db
import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, Float, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

load_dotenv()
DBpath = os.path.join(os.path.dirname(f'{os.getenv("SQLite_PATH")}'), f'{os.getenv("SQLite_NAME")}')
SQLite_BIN = create_engine(f'sqlite:///{DBpath}')
Base = declarative_base()

#==========Classes para o db==========
class Servidor(Base):
    """Classe que representa o mundo/servidor criado"""
    __tablename__ = "servidor"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)

    #Seleciona as dimensões do servidor
    dimension = relationship("Dimensao")

class Dimensao(Base):
    """Classe que representa a dimensão que o personagem está"""
    __tablename__ = "dimensao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_server = Column(Integer, ForeignKey('servidor.id'))
    nome = Column(String(40))

    #Seleciona os locais da dimensão
    local_name = relationship("Local", back_populates="dimension")

class Local(Base):
    """Classe que representa o local que a coordenada aponta (nome da coordenada)"""
    __tablename__ = "local"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_server = Column(Integer, ForeignKey('servidor.id'))
    id_dim = Column(Integer, ForeignKey('dimensao.id'))
    nome = Column(String(50), nullable=False)

    #Seleciona as dimensões do local
    #Seleciona as coordenadas do local
    dimension = relationship("Dimensao", back_populates="local_name")
    coord = relationship("Coordenada", back_populates="local")

class Coordenada(Base):
    """Tabela que indica a posição geográfica do personagem"""
    __tablename__ = "coordenada"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_server = Column(Integer, ForeignKey('servidor.id'))
    id_dim = Column(Integer, ForeignKey('dimensao.id'))
    id_local = Column(Integer, ForeignKey('local.id'))
    x = Column("x", Float, nullable=False)
    y = Column("y", Float, nullable=False)
    z = Column("z", Float, nullable=False)

    #Seleciona os locais da coordenada
    local = relationship("Local", back_populates="coord")

#Cria as tabelas no BD
def criar_tabelas_sqlite():
    """Método para criar as tabelas SQLite do db."""
    Base.metadata.create_all(bind=SQLite_BIN)

#Cria conexão com o BD
def conectar_sqlite_bd():
    """Método para criar conexão com o BD."""
    session = sessionmaker(bind=SQLite_BIN)
    return session()

#==========Métodos para o BD==========
def commit_coordenada(srv_name:str, dim_name:str, local_name:str, coor_x:float, coor_y:float, coor_z:float) -> str:
    """Função para pegar as coordenadas do Minecraft."""
    session = conectar_sqlite_bd()

    servidor: Servidor = session.query(Servidor).filter_by(nome=srv_name).first()
    if not servidor:
        servidor = Servidor(nome=srv_name)
        session.add(servidor)
        session.commit()

    dimensao: Dimensao = session.query(Dimensao).filter_by(nome=dim_name, id_server=servidor.id).first()
    if not dimensao:
        dimensao = Dimensao(nome=dim_name, id_server=servidor.id)
        session.add(dimensao)
        session.commit()

    local: Local = session.query(Local).filter_by(nome=local_name, id_dim=dimensao.id).first()
    if not local:
        local = Local(nome=local_name, id_server=servidor.id, id_dim=dimensao.id)
        session.add(local)
        session.commit()

    coordenada: Coordenada = Coordenada(
        id_server=servidor.id,
        id_dim=dimensao.id,
        id_local=local.id,
        x=coor_x, y=coor_y, z=coor_z
    )

    session.add(coordenada)
    session.commit()
    session.close()

    return f'Coordenadas de {dim_name}-{local_name} foram salvas com sucesso no servidor {srv_name}!'

def check_existence(server_name:str, dim_name:str, local_name:str, coor_x:float, coor_y:float, coor_z:float) -> bool:
    """Método para verificar se a coordenada existe."""
    #Cria conexão com o BD
    session = conectar_sqlite_bd()

    servidor = session.query(Servidor).filter_by(nome=server_name).first()
    if not servidor:
        return False

    dim = session.query(Dimensao).filter_by(nome=dim_name, id_server=servidor.id).first()
    if not dim:
        return False

    local = session.query(Local).filter_by(nome=local_name, id_dim=dim.id, id_server=servidor.id).first()
    if not local:
        return False

    #Pega as coordenadas do banco e verifica duplicata
    exists = session.query(Coordenada).filter_by(
        id_server=servidor.id,
        id_dim=dim.id,
        id_local=local.id,
        x=coor_x,
        y=coor_y,
        z=coor_z
    ).first() is not None
    session.close()

    return exists
