"""ARQUIVO RESPONSÁVEL PELA VALIDAÇÃO DE DADOS.(_validador)"""
import re
from .utils import Union

class Validador:
    """Classe que controla os validadores."""
    @staticmethod
    def validar_string(valor: str, nome: str) -> bool:
        """Valida se o valor é uma string não-vazia."""
        if not isinstance(valor, str) and valor != (["Servidor", "Nome"]):
            raise ValueError(f'"{nome}" deve ser uma string e campo não pode ser vazio.')

        if valor == (["Servidor", "Nome"]):
            valor = "Desconhecido"

        return True

    @staticmethod
    def validar_int(valor: int, nome: str) -> bool:
        """Valida se o valor é inteiro."""
        if not isinstance(valor, int) or valor == 0:
            raise ValueError(f'"{nome}" deve ser um valor inteiro diferente de 0.')

        return True

    @staticmethod
    def validar_world(valor:str, nome: str) -> bool:
        """Valida se 'World' possui os dados corretos."""
        MUNDOS = tuple[str, str](["Overworld", "Nether", "End"])

        if valor not in MUNDOS:
            raise ValueError(f'"{nome}" deve ser um desses\n{MUNDOS}.')

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
