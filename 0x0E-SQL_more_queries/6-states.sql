--- create a ccdb and a user
-- in the db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the db
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
