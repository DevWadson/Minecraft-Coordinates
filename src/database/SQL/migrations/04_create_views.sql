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

-- View para listar coordenadas pelo nome do local
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
