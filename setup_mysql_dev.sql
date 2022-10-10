-- Create new database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create new user hbnb_dev
CREATE IF NOT EXISTS USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant hbnb_dev all priveldge on hbnb_dv_db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
