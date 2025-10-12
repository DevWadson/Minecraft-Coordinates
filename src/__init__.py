"""Inicializa e organiza os módulos do Minecraft Coordinates.

Este módulo importa todas as funções e classes do código principal,
permitindo uma referência centralizada para execução da aplicação,
interface gráfica, validações e utilitários.

Elementos incluídos:
- main.py: ponto de entrada da aplicação
- gui.py: interface gráfica
- overview.py: visão geral da aplicação
- validador.py: funções de validação
- utils.py: funções auxiliares
- config.py: parâmetros e constantes de configuração
"""
from .gui import GUI
from .validador import Validador
from . import utils

from .database import (
    Servidor,
    Dimensao,
    Local,
    Coordenada,
    SQL,
    conectar_sqlite_bd,
    criar_tabelas_sqlite,
    commit_coordenada,
    check_existence
)
