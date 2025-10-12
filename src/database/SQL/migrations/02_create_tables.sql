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
    id_dim INT UNSIGNED,
    nome VARCHAR(50),
    FOREIGN KEY (id_server) REFERENCES servidor(id), -- O local está no servidor criado
    FOREIGN KEY (id_dim) REFERENCES dimensao(id) -- O local está na dimensão que o personagem está, que está no servidor criado
);

-- Tabela que indica a posição geográfica do personagem
CREATE TABLE IF NOT EXISTS coordenada(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_server INT UNSIGNED,
    id_dim INT UNSIGNED,
    id_local INT UNSIGNED,
    x FLOAT,
    y FLOAT,
    z FLOAT,
    FOREIGN KEY (id_server) REFERENCES servidor(id), -- A coordenada está no servidor criado
    FOREIGN KEY (id_dim) REFERENCES dimensao(id), -- A coordenada está na dimensão definida, que está no servidor
    FOREIGN KEY (id_local) REFERENCES local(id) -- A coordenada referencia o local do personagem, que está no servidor
);
