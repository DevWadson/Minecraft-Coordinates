"""
Módulo de conexão com o banco MySQL usando SQLAlchemy.

Este módulo cria uma engine e uma função para gerar sessões SQLAlchemy
aproveitando as configurações definidas em src/config.py e as variáveis
de ambiente do arquivo .env.

A função `conectar_mysql()` retorna uma sessão pronta para consultas
e operações no banco MySQL.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from src.config import MySQLConfig

load_dotenv()

db_config = MySQLConfig()
db_config.iniciar()

MYSQL_CONN = f"mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PSSWRD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}"
MySQL_BIN = create_engine(MYSQL_CONN, echo=True)

def conectar_mysql():
    """Retorna uma sessão SQLAlchemy"""
    Session = sessionmaker(bind=MySQL_BIN)

    return Session()
