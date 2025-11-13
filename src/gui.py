"""ARQUIVO REFATORADO QUE REPRESENTA A GUI DO PROGRAMA (_gui)."""
import customtkinter as ctk
import pandas as pd
from src.database.SQL.models import Servidor, Dimensao, Local, Coordenada
from src.database.SQL.schemas import ServidorCreate, DimensaoCreate, LocalCreate, CoordenadaCreate
from src.database.SQL.mysql_connection import (
    commit_servidor,
    commit_dimensao,
    commit_local,
    commit_coordenada,
    SessionLocal
)
# from src.database.SQLite import commit_coordenada, check_existence
from .utils import buscar_local, clear_frame, criar_botao, selected_option
from .validador import Validador

class GUI:
    """Classe responsável pela interface gráfica do programa."""
    def __init__(self) -> None:
        """Cria a interface gráfica."""
        self.janela = self.ajustar_janela()
        self.widget = self.criar_widgets()

    def ajustar_janela(self):
        """Cria a interface gráfica."""
    #Criando e ajustando a tela
        janela = ctk.CTk()
        janela.title("Coletor de Coordenadas")
        janela.geometry("1000x600")

        return janela

    def criar_widgets(self):
        """Cria e organiza todos os widgets da interface."""
        clear_frame()
    #Cabeçalho
        self.header = ctk.CTkLabel(self.janela, text="Formulário", font=("Times New Roman", 20))
        self.header.pack(pady=10)

    #Frame vazio da janela
        self.dados = ctk.CTkLabel(self.janela, text="")
        self.dados.pack(pady=10)

    #Entries
        self.server_entry = self.criar_entry("Servidor")
        self.dimension_entry = self.criar_entry("Dimensão")
        self.local_entry = self.criar_entry("Nome da Coordenada")
        self.x_entry = self.criar_entry("Coordenada X")
        self.y_entry = self.criar_entry("Coordenada Y")
        self.z_entry = self.criar_entry("Coordenada Z")

    #Menu Lateral Inferior
        self.menu = ctk.CTkFrame(self.janela, width=200, corner_radius=10)
        self.menu.pack(side="left", fill="y", padx=10, pady=10)

    #Botões
        self.botao_save = criar_botao(self.janela, "Salvar Coordenada", self.salvar_coord_info)

        self.botao_show = criar_botao(self.menu, "Ver Coordenadas", command=self.show_coor)

        self.botao_search = criar_botao(self.menu, text="Procurar Coordenada", command=self.search_coor)

    #Frame para exibição das coordenadas
        self.conteudo_frame = ctk.CTkFrame(self.janela)
        self.conteudo_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.conteudo = ctk.CTkLabel(self.conteudo_frame, text="")
        self.conteudo.pack(pady=20)

        self.scroll_bar = ctk.CTkScrollableFrame(width=3, master=self.conteudo_frame)
        self.scroll_bar.pack(side="right", pady=1)

        return self.criar_widgets

    def criar_entry(self, placeholder_text:str) -> ctk.CTkEntry:
        """Cria campos de input."""
        entry = ctk.CTkEntry(self.janela, placeholder_text=placeholder_text)
        entry.pack(padx=5, pady=10)

        return entry

#==========Métodos para a interface gráfica==========
    def abrir_tela(self):
        """Método responsável por criar a interface gráfica."""
        self.janela.mainloop()

    def coletar_coor(self) -> tuple:
        """Método para coletar as coordenadas.""" #TODO: Refactor
        new_server = ServidorCreate(nome=self.server_entry.get())
        new_dimension = DimensaoCreate(nome=self.dimension_entry.get())
        new_local = LocalCreate(nome=self.local_entry.get())
        new_coord = CoordenadaCreate(
            x=float(self.x_entry.get()),
            y=float(self.y_entry.get()),
            z=float(self.z_entry.get())
        )

        return (new_server, new_dimension, new_local, new_coord)

    def limpar_campos(self):
        """Limpa os campos de entrada."""
        for entry in [self.server_entry,
                        self.dimension_entry,
                        self.local_entry,
                        self.x_entry,
                        self.y_entry,
                        self.z_entry
                        ]:
            entry.delete(0, "end")
        return

    def salvar_coord_info(self):
        """Método para salvar as coordenadas."""
        server_schema, dimension_schema, local_schema, coordenada_schema = self.coletar_coor()

        if not self.validate_entries(server_schema.nome, dimension_schema.nome, local_schema.nome, coordenada_schema):
            self.janela.after(2000, self.limpar_mensagem) # 2000ms = 2 segundos

        else:
            servidor = commit_servidor(server_schema)
            dimensao = commit_dimensao(dimension_schema, servidor.id)
            local = commit_local(local_schema, servidor.id, dimensao.id)
            coordenada = commit_coordenada(coordenada_schema, servidor.id, dimensao.id, local.id)

            self.limpar_campos()
            self.dados.configure(text=f'Coordenada "{local.nome}" salva com sucesso!')
            self.janela.after(2000, self.limpar_mensagem)

    def validate_entries(self, server: Servidor, world: Dimensao, nome: Local, coordinate: Coordenada) -> bool:
        """Método para validar as entradas."""
        valid_serv = Validador.validar_string(server, "Servidor")
        valid_wrld = Validador.validar_world(world, "Dimensão")
        valid_nome = Validador.validar_string(nome, "Nome da Coordenada")
        valid_cx = Validador.validar_coord(coordinate.x, "Coordenada X")
        valid_cy = Validador.validar_coord(coordinate.y, "Coordenada Y")
        valid_cz = Validador.validar_coord(coordinate.z, "Coordenada Z")

        validador = [valid_serv, valid_wrld, valid_nome, valid_cx, valid_cy, valid_cz]

        if not all(validador):
            self.dados.configure(text="Entrada inválida!")

        #Verificando se todos os campos foram preenchidos
        if not world or not nome or not coordinate:
            self.dados.configure(text="Todos os campos devem ser preenchidos!")

        return True

    # DA PRA MELHORAR MAIS!!!!!!!!!!
    def show_coor(self):
        """Método para mostrar as coordenadas salvas."""
        self.conteudo.configure(text="Coordenadas Salvas") #TÍTULO

    # Limpa o frame anterior
        clear_frame()

        # session = SessionLocal()

        # coordenada = session.query(Coordenada).all()

        #Converte as coordenadas para um objeto
        coordenadas_all = [
            {
                'Servidor': coor.id_server,
                'Dimensao': coor.id_dim,
                'Local': coor.local,
                'x': coor.x,
                'y': coor.y,
                'z': coor.z
            }
            for coor in coordenada
        ]

        #Converte o obeto em um dataframe
        coord_info_df: pd.DataFrame = pd.DataFrame(coordenadas_all)

        # Cria uma caixa de texto para exibir as coordenadas
        text_box: ctk.CTkTextbox = ctk.CTkTextbox(self.conteudo_frame, width=600, height=300)
        text_box.pack(pady=10)

        # Verifica se a caixa de texto ainda existe
        if not hasattr(self, "text_box") or not text_box.winfo_exists():
            pass
        else:
            text_box.configure(state="normal") #HABILITA A CAIXA
            text_box.delete("1.0", "end")

        #Converte o dataframe para uma tabela estilizada
        coord_str = coord_info_df.to_string(index=True, justify="center", col_space=10)

        #Anexa as coordenadas ao frame
        if coord_info_df.empty:
            self.conteudo.configure(text="Nenhuma coordenada salva") #REESCRITA DO TÍTULO

        else:
            text_box.insert("1.0", f'\n{coord_str}')
            text_box.configure(state="disabled")

    def search_coor(self):
        """Método para procurar as coordenadas salvas."""
        self.conteudo.configure(text="Procurar Coordenada")

        clear_frame()

        menu = ctk.CTkOptionMenu(
            self.conteudo_frame,
            values=[
                "Selecione",
                "Servidor",
                "Local"
            ],
            command=selected_option
        ).pack(pady=10)

        botao_search: ctk.CTkButton = criar_botao(self.conteudo_frame, "Buscar", buscar_local)

    def limpar_mensagem(self):
        """Método para limpar a mensagem."""
        self.dados.configure(text="")
