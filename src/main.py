"""Programa para guardar coordenadas do Minecraft.(_main)"""
# from database import criar_tabelas_sqlite
from database.SQL.mysql_conection import conectar_mysql
from . import GUI

#==========Função Principal==========
def main():
    """Início do programa."""
# ==========DECLARAÇÕES=========
    tela = GUI()
    mysql_conn = conectar_mysql()

# ==========COMANDOS==========
    # criar_tabelas_sqlite() # SQLite

    tela.abrir_tela()

    mysql_conn.close()

if __name__ == "__main__":
    main()
