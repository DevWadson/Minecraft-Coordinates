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

from src.database.SQL.schemas import (
    ServidorBase, ServidorCreate, ServidorResponse,
    DimensaoBase, DimensaoCreate, DimensaoResponse,
    LocalBase, LocalCreate, LocalResponse,
    CoordenadaBase, CoordenadaCreate, CooredenadaResponse
)

load_dotenv()

MYSQL_CONN = f"mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PSSWRD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}"
MySQL_BIN = create_engine(MYSQL_CONN, echo=True)
SessionLocal = sessionmaker(bind=MySQL_BIN)

def get_mysql_db() -> Generator[Session, None, None]:
    """Retorna uma sessão SQLAlchemy"""
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

Base.metadata.create_all(bind=MySQL_BIN)

with MySQL_BIN.connect() as conexao:
    print("Conexão bem sucedida!")
