-- Create new database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create new user hbnb_dev
CREATE IF NOT EXISTS USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant hbnb_dev all priveldge on hbnb_dv_db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Create new database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create new user hbnb_test
CREATE IF NOT EXISTS USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant hbnb_test all priveldge on hbnb_dv_db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
