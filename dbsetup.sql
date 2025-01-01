-- Creates the ExploreKe development database
CREATE DATABASE IF NOT EXISTS exploreKe;
CREATE USER IF NOT EXISTS 'devbrian'@'localhost' IDENTIFIED BY 'exploreKe_pwd';
GRANT ALL PRIVILEGES ON exploreKe_db.* TO 'devbrian'@'localhost';
GRANT SELECT ON performance_schema.* TO 'devbrian'@'localhost';
FLUSH PRIVILEGES;