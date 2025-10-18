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
DELIMITER ; -- Restaura o delimitador

-- Gatilho para verificar se a coordenada já existe
DELIMITER //
CREATE TRIGGER checar_duplo_local
	BEFORE INSERT ON local
		FOR EACH ROW
			BEGIN
				DECLARE err_msg VARCHAR(255);
				IF EXISTS(
					SELECT 1 FROM local
						WHERE
							id_server=NEW.id_server AND
							id_dim=NEW.id_dim AND
							nome=NEW.nome
					) THEN
						SET err_msg = concat('Coordenada ', NEW.nome, ' já existe no banco!');
						SIGNAL SQLSTATE '45000'
							SET MESSAGE_TEXT = err_msg;
				END IF;
			END ;
//
DELIMITER ;
