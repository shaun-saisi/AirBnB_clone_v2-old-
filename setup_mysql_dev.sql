-- This file prepares a script for MYSQL server
-- Create a database  hbnb_dev_db.
-- A user hbnb at localhost
-- Grants all privileges to the user
-- Grants select privileges on perfomance

-- Create database 
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'Callais7461!';
-- Grant all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Select privileges on perfomance
GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
