"""
Módulo de conexão com o banco MySQL usando SQLAlchemy.

Este módulo cria uma engine e uma função para gerar sessões SQLAlchemy
aproveitando as configurações definidas em src/config.py e as variáveis
de ambiente do arquivo .env.

A função `conectar_mysql()` retorna uma sessão pronta para consultas
e operações no banco MySQL.
"""
import os
from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from dotenv import load_dotenv
from src.database.SQL.base import Base
from src.database.SQL.models import Servidor, Dimensao, Local, Coordenada
from src.database.SQL.schemas import ServidorCreate, DimensaoCreate, LocalCreate, CoordenadaCreate

load_dotenv()

MYSQL_CONN = f'mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PSSWRD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}'
MySQL_BIN = create_engine(MYSQL_CONN, echo=True)
SessionLocal = sessionmaker(bind=MySQL_BIN)

#==========Conexão com o banco MySQL==========
@contextmanager
def get_mysql_db() -> Generator[Session, None, None]:
    """Retorna uma sessão SQLAlchemy"""
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

#==========Criação das tabelas==========
def criar_tabelas_mysql():
    """Cria as tabelas no banco MySQL."""
    Base.metadata.create_all(bind=MySQL_BIN)

#==========Métodos para o banco MySQL==========
def commit_servidor(servidor_schema: ServidorCreate) -> Servidor:
    """Comitta o servidor no banco MySQL."""
    servidor = Servidor(**servidor_schema.model_dump())

    with get_mysql_db() as db:
        db.add(servidor)
        db.flush()
        db.commit()
        db.refresh(servidor)
        print(f'Após refresh: servidor.id = {servidor.id}')
    return servidor

def commit_dimensao(dimensao_schema: DimensaoCreate, id_server:int) -> Dimensao:
    """Comitta a dimensão no banco MySQL"""
    dimensao = Dimensao(**dimensao_schema.model_dump(), id_server=id_server)

    with get_mysql_db() as db:
        db.add(dimensao)
        db.flush()
        db.commit()
        db.refresh(dimensao)

    return dimensao

def commit_local(local_schema: LocalCreate, id_server:int, id_dim:int) -> Local:
    """Comitta o local no banco MySQL"""
    local = Local(**local_schema.model_dump(), id_server=id_server, id_dim=id_dim)

    with get_mysql_db() as db:
        db.add(local)
        db.flush()
        db.commit()
        db.refresh(local)

    return local

def commit_coordenada(coordenada_schema: CoordenadaCreate, id_server:int, id_dim:int, id_local:int) -> Coordenada:
    """Comitta a coordenada no banco MySQL"""
    coordenada = Coordenada(**coordenada_schema.model_dump(), id_server=id_server, id_dim=id_dim, id_local=id_local)

    with get_mysql_db() as db:
        db.add(coordenada)
        db.flush()
        db.commit()
        db.refresh(coordenada)

    return coordenada

#==========Teste de conexão==========
with MySQL_BIN.connect() as conexao:
    print("Conexão bem sucedida!")
