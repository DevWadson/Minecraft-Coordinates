"""ARQUIVO DE CONFIGURAÇÕES.(_config)"""
#==========IMPORTS==========
import os
from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv

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

        return mysql.__init__(app)

#'/_gui/'
ONE_SECOND = 1000
TWO_SECOND = 2000
THREE_SECOND = 3000
FOUR_SECOND = 4000
FIVE_SECOND = 5000
SIX_SECOND = 6000
SEVEN_SECOND = 7000
EIGHT_SECOND = 8000
NINE_SECOND = 9000
TEN_SECOND = 10000
