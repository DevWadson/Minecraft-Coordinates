# Documentação do Projeto: Coordenadas do Minecraft

Descrição Geral

    Este projeto tem como objetivo criar um programa em Python para gerenciar coordenadas de locais no Minecraft. Ele utiliza um banco de dados para armazenar informações sobre servidores, dimensaos e coordenadas específicas, além de fornecer uma interface gráfica para facilitar o uso.

Funcionalidades

1. Gerenciamento de Coordenadas

    Armazenamento no Banco de Dados:

        Armazena informações como servidor, dimensao, local e coordenadas X, Y e Z no banco de dados SQLite.

    Interface Gráfica:

        Utiliza customtkinter para criar uma interface amigável para entrada e exibição de dados.

    Exibição de Coordenadas:

        Mostra as coordenadas salvas no banco de dados em formato de tabela utilizando o pandas.

Componentes do Projeto

1. Banco de Dados

    O banco de dados é gerenciado por SQLite e definido com a biblioteca SQLAlchemy.

    Tabela principal:

        Coordenadas

    Campos:

        id (Integer): Identificador único.

        servidor (String): Nome do servidor.

        dimensao (String): Nome da dimensão (Overworld, Nether ou Stronghold).

        local (String): Nome do local.

        coor_x, coor_y, coor_z (Float): Coordenadas do local.

   2. Interface Gráfica

       A interface gráfica é implementada com customtkinter e inclui:

           Entradas para servidor, dimensao, local e coordenadas (X, Y, Z).

           Botão para salvar coordenadas no banco de dados.

           Botão para visualizar todas as coordenadas salvas.

      3. Classes e Funções

          Classe Coordenadas

              Representa o modelo de dados para o banco de dados.

          Classe GUI

              Gerencia a interface gráfica do programa.

              Métodos principais:

                  abrir_tela():
                     Inicia o loop principal da interface.

                  coletar_e_salvar_coor():
                     Coleta os dados das entradas e salva no banco de dados.

                  limpar_mensagem():
                     Limpa mensagens exibidas na interface.

                  show_coor():
                     Mostra as coordenadas salvas no banco de dados em um formato tabular.

                  pegar_coordenadas():
                     Adiciona coordenadas ao banco de dados e retorna uma mensagem de sucesso.

                  main()
                     Função principal que inicializa o programa e a interface gráfica.

Tecnologias Utilizadas

    Linguagem de Programação

        Python 3.10 ou superior

    Bibliotecas

        os: Para manipulação de caminhos e arquivos.

        pandas: Para manipulação e exibição de dados em tabelas.

        customtkinter: Para a interface gráfica.

        sqlalchemy: Para a criação e gerenciamento do banco de dados.

Exemplo de Fluxo de Uso

    ➡️Início do Programa:

        O programa exibe uma mensagem personalizada para o autor.

        ➡️Inserção de Coordenadas:

            O usuário insere as informações do servidor, dimensão, local e coordenadas (X, Y, Z).

        ➡️Armazenamento no Banco de Dados:

            Os dados inseridos são salvos no banco de dados.

        ➡️Exibição das Coordenadas:

            O usuário pode visualizar todas as coordenadas salvas em formato tabular na interface gráfica.

Requisitos

    Tecnologias Necessárias

        Python 3.10 ou superior

Dependências

    Instale as bibliotecas necessárias com o comando:

        pip install pandas customtkinter sqlalchemy

Contato

    Para mais informações, entre em contato com o autor:

        Autor: Marlon

        E-mail: [marlonwadson.dev@gmail.com]

        WhatsApp: [71 9 8635-3910]
