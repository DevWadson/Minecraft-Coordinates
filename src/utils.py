"""ARQUIVO DE UTILIDADES.(_utils)"""
#==========Imports==========
from typing import Union, Callable, Any
import customtkinter as ctk
from .database.SQLite.sqlite_db_script import Servidor, Coordenada, Local
from .config import session

def clear_frame() -> None:
    """Método para limpar os atributos do frame."""
    frame: ctk.CTkFrame = ctk.CTkFrame(ctk.CTk())
    conteudo: ctk.CTkLabel = ctk.CTkLabel(frame)

    for widget in frame.winfo_children():
        if widget != conteudo:
            widget.destroy()

    return

def selected_option(option:str):
    """Método para lidar com a seleção do menu."""
    if option == "Selecione":
        return None

    if option == "Servidor":
        return session.query(Servidor.nome).all()

    if option == "Local": #Procura o nome digitado na entry, no banco
        return buscar_local()

    return option

def buscar_local() -> Coordenada:
    """Método para procurar os locais salvos."""
    nome: ctk.CTkEntry = ctk.CTkEntry(ctk.CTk(), placeholder_text="")

    return (session.query(Coordenada)
            .join(Local, Coordenada.id_local == Local.id)
            .filter(Local.nome == nome)
            .first())

def criar_botao(inserted_on:Any, text:str, command: Union[Callable[[], Any], None]) -> ctk.CTkButton:
    """Método para criar um botão."""
    botao = ctk.CTkButton(inserted_on, text=text, command=command)
    botao.pack(padx=10, pady=20)

    return botao
