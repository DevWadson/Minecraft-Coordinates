"""Programa para guardar coordenadas do Minecraft.(_main)"""
# from .database import criar_tabelas_sqlite
# from .database.SQLite.sqlite_db_script import criar_tabelas_sqlite
from .database.SQL.mysql_connection import get_mysql_db
from . import GUI

#==========Função Principal==========
def main():
    """Início do programa."""
#==========DECLARAÇÕES=========
    tela = GUI()
    mysql_conn = get_mysql_db()

#==========COMANDOS==========
    # criar_tabelas_sqlite()

    tela.abrir_tela()

    mysql_conn.close()

if __name__ == "__main__":
    main()
