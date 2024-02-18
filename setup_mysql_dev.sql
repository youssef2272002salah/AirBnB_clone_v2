CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE User IF NOT EXISTS 'hbnb_dev'@'localhost' identified by 'hbnb_dev_pwd';
grand all privileges on 'hbnb_dev_db'.* to 'hbnb_dev'@'localhost';
grand select on 'performance_schema'.* to 'hbnb_dev'@'localhost';
flush privileges;

