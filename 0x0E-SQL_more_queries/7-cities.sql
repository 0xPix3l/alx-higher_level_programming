-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABSE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	`id` INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`state_id` INT NUT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	`name VARCHAR(256) NOT NULL
	);
