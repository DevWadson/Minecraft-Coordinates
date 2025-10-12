"""
Declaração da base para os modelos do SQLAlchemy.

Define a instância base utilizada por todos os modelos ORM da aplicação.
"""
from sqlalchemy.orm import declarative_base

Base = declarative_base()
