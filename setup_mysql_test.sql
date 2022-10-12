-- Create new database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create new user hbnb_test
CREATE USER IF NOT EXISTS'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant hbnb_test all priveldge on hbnb_dv_db
USE hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;