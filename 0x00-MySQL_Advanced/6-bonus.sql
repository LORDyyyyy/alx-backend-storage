-- a SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(IN id INT, IN porj_name VARCHAR(255), IN score INT)
BEGIN
    IF NOT EXISTS (SELECT name FROM projects WHERE name = porj_name) THEN
        INSERT INTO projects (name) VALUES (porj_name);
    END IF;
    INSERT INTO corrections VALUES (id, (SELECT id FROM projects WHERE name = porj_name), score);
END; $$
DELIMITER ;
