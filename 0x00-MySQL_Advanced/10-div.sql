-- a SQL script that creates a function SafeDiv
-- that divides (and returns) the first by the second number or returns 0
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE res FLOAT;
    IF b = 0 THEN
        SET res = 0;
    ELSE
        SET res = (a * 1.0) / b;
    END IF;
    RETURN res;
END $$
DELIMITER ;
