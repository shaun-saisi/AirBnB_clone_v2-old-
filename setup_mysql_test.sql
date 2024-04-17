-- This file creates a mysql server with:
-- A user, granted all privileges.
-- Select privileges on perfomance schema.

-- Creates the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Select privileges
GRANT SELECT ON perfomance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
