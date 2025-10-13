"""ARQUIVO DE CONFIGURAÇÕES.(_config)"""
#==========IMPORTS==========
from sqlalchemy.orm import Session
from src.database.SQL.models import Coordenada
from src.database.SQL import get_mysql_db

#==========Declarações Globais==========
session: Session = next(get_mysql_db()) #SQL
coordenada = session.query(Coordenada).all()
