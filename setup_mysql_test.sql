-- Create the database hbnb_test_db
-- Create the user hbnb_test
-- All privileges granted on the database hbnb_test_db to the user hbnb_test
-- SELECT privileges granted on the database performance_schema 
-- to the user hbnb_test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
