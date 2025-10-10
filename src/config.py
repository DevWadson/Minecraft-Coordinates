"""ARQUIVO DE CONFIGURAÇÕES.(_config)"""
#==========IMPORTS==========
import os
from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from database.SQLite.sqlite_db_script import Coordenada
from database.SQL.mysql_conection import conectar_mysql

#==========Declarações Globais==========
load_dotenv()
app = Flask(__name__)
mysql = MySQL()

#'/_main/'
class MySQLConfig:
    """Configurações do MySQL"""
    def iniciar(self):
        """Gerencia a configuração com o banco"""
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        psswrd = os.getenv("DB_PSSWRD")
        name = os.getenv("DB_NAME")

        app.config['MYSQL_HOST'] = host
        app.config['MYSQL_USER'] = user
        app.config['MYSQL_PASSWORD'] = psswrd
        app.config['MYSQL_DB'] = name

        return app

session = conectar_mysql()
coordenada = session.query(Coordenada).all()
