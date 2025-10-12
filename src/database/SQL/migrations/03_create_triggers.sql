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
