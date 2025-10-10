CREATE DATABASE IF NOT EXISTS Coordenadas_Mine_db;

USE Coordenadas_Mine_db;

-- Tabela que representa o mundo/servidor criado
CREATE TABLE IF NOT EXISTS servidor(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(120) NOT NULL
);

-- Tabela que representa a dimensão que o personagem está
CREATE TABLE IF NOT EXISTS dimensao(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_server INT UNSIGNED,
    nome VARCHAR(40),
    FOREIGN KEY (id_server) REFERENCES servidor(id) -- A dimensão está no servidor criado
);

-- Tabela que representa o local que a coordenada aponta (nome da coordenada)
CREATE TABLE IF NOT EXISTS local(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_server INT UNSIGNED,
    id_dimen INT UNSIGNED,
    nome VARCHAR(50),
    FOREIGN KEY (id_server) REFERENCES servidor(id), -- O local está no servidor criado
    FOREIGN KEY (id_dimen) REFERENCES dimensao(id) -- O local está na dimensão que o personagem está, que está no servidor criado
);

-- Tabela que indica a posição geográfica do personagem
CREATE TABLE IF NOT EXISTS coordenada(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_server INT UNSIGNED,
    id_dimensao INT UNSIGNED,
    id_local INT UNSIGNED,
    x FLOAT,
    y FLOAT,
    z FLOAT,
    FOREIGN KEY (id_server) REFERENCES servidor(id), -- A coordenada está no servidor criado
    FOREIGN KEY (id_dimensao) REFERENCES dimensao(id), -- A coordenada está na dimensão definida, que está no servidor
    FOREIGN KEY (id_local) REFERENCES local(id) -- A coordenada referencia o local do personagem, que está no servidor
);

-- Muda o delimitador para '//' para o comando funcionar corretamente
DELIMITER //
-- Gatilho para validar o valor de 'Dimensao'
CREATE TRIGGER ValidarDimensao
	BEFORE INSERT ON dimensao
		FOR EACH ROW
			BEGIN
				IF NEW.nome NOT IN ("Overworld", "Nether", "End") THEN
					SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Dimensão não válida! Deve ser "Overworld", "Nether", ou "End"'; 	
				END IF;
			END;
//
DElIMITER ; -- Restaura o delimitador

-- View para listar coordenadas pelo nome do servidor
CREATE VIEW CoordenadaPorServer AS
	SELECT
		c.id, -- ID da coordenada
        s.nome AS servidor,
        l.nome AS nome_coordenada,
        c.x,
        c.y,
        c.z
	FROM coordenada c
		JOIN servidor s ON c.id_server=s.id -- "Associe os registros de Coordenada no 'id_server' que seja igual ao id do Servidor"
        JOIN local l on c.id_local=l.id
        ORDER BY s.nome;

-- View para listar coordenadas pelo nome da coordenada
CREATE VIEW CoordenadaPorNome AS
	SELECT
		c.id, -- ID da Coordenada
        l.nome AS nome_coordenada,
        c.x,
        c.y,
        c.z
	FROM coordenada c
		JOIN local l ON c.id_local=l.id -- "Associe os registros de Coordenada no 'id_local' que seja igual ao id do Local"
        ORDER BY l.nome;

SELECT * FROM CoordenadaPorNome;
SELECT * FROM CoordenadaPorServer;
SELECT * FROM Servidor;
SELECT * FROM Dimensao;
SELECT * FROM Local;
SELECT * FROM Coordenada;
