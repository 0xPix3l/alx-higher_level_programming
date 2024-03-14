-- script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS (`id` INT DEFAULT 1, 
	UNIQUE(ID), 
	NAME VARCHAR(256));
