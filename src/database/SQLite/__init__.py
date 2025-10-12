"""
Pacote SQLite para configuração do banco de dados.

Contém engine, sessões, base declarativa e scripts de inicialização.
"""
from .sqlite_db_script import (
    Servidor,
    Dimensao,
    Local,
    Coordenada,
    criar_tabelas_sqlite,
    commit_coordenada,
    check_existence,
    conectar_sqlite_bd,
    Base,
    SQLite_BIN
)
