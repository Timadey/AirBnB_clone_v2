-- Create new database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create new user hbnb_test
CREATE IF NOT EXISTS USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant hbnb_test all priveldge on hbnb_dv_db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';