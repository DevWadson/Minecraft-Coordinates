"""
Módulo de conexão com o banco MySQL usando SQLAlchemy.

Este módulo cria uma engine e uma função para gerar sessões SQLAlchemy
aproveitando as configurações definidas em src/config.py e as variáveis
de ambiente do arquivo .env.

A função `conectar_mysql()` retorna uma sessão pronta para consultas
e operações no banco MySQL.
"""
import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from dotenv import load_dotenv
from src.database.SQL.base import Base
from src.database.SQL.models import Servidor, Dimensao, Local, Coordenada

load_dotenv()

MYSQL_CONN = f"mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PSSWRD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}"
MySQL_BIN = create_engine(MYSQL_CONN, echo=True)
SessionLocal = sessionmaker(bind=MySQL_BIN)

#==========Conexão com o banco MySQL==========
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
def commit_servidor(servidor: Servidor) -> Servidor:
    """Comitta o servidor no banco MySQL."""
    with get_mysql_db() as db:
        db.add(servidor)
        db.commit(servidor)
        db.refresh(servidor)

    return servidor

def commit_dimensao(dimensao: Dimensao) -> Dimensao:
    """Comitta a dimensão no banco MySQL"""
    with get_mysql_db() as db:
        db.add(dimensao)
        db.commit(dimensao)
        db.refresh(dimensao)

    return dimensao

def commit_local(local: Local) -> Local:
    """Comitta o local no banco MySQL"""
    with get_mysql_db() as db:
        db.add(local)
        db.commit(local)
        db.refresh(local)

    return local

def commit_coordenada(coordenada: Coordenada) -> Coordenada:
    """Comitta a coordenada no banco MySQL"""
    with get_mysql_db() as db:
        db.add(coordenada)
        db.commit(coordenada)
        db.refresh(coordenada)

    return coordenada

#==========Teste de conexão==========
with MySQL_BIN.connect() as conexao:
    print("Conexão bem sucedida!")
