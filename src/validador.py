"""ARQUIVO RESPONSÁVEL PELA VALIDAÇÃO DE DADOS.(_validador)"""
import re
from .utils import Union

class Validador:
    """Classe que controla os validadores."""
    @staticmethod
    def validar_string(valor: str, nome: str) -> bool: #Trocar para 'normalizar_string'
        """Verifica se o campo é vazio."""
        if nome in ("Servidor", "Nome") and valor == "":
            valor = "Desconhecido"

            return valor

        return True

    @staticmethod
    def validar_world(valor:str, nome: str) -> bool:
        """Valida se 'World' possui os dados corretos."""
        mundos = {"Overworld", "Nether", "End"}

        if valor not in mundos:
            raise ValueError(f'"{nome}" deve ser um desses\n{mundos}.')

        return True

    @staticmethod
    def validar_coord(valor: Union[str, float], nome:str) -> bool:
        """Valida a coordenada."""
        valor = str(valor)

        if re.match(r"^-?\d{2,}+(\.\d+)?$", valor):
            pass

        else:
            raise ValueError(f'"{nome}" deve ter, pelo menos, 2 dígitos.')

        return True
