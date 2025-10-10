"""
Inicialização do pacote de banco de dados.

Importa e centraliza os objetos essenciais de conexão, modelos e schemas
utilizados em toda a aplicação para facilitar o acesso e organização.
"""
from .SQLite import (
    SQLite_BIN,               # engine SQLite
    Base,             # declarative_base
    Servidor,
    Dimensao,
    Local,
    Coordenada,
    criar_tabelas_sqlite,
    conectar_sqlite_bd,
    commit_coordenada,
    check_existence
)
