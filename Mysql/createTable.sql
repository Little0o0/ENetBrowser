
CREATE DATABASE ENetDB;

use ENetDB;

CREATE TABLE IF NOT EXISTS `dataTable`(
   `id` INT UNSIGNED,
   `question` VARCHAR(500) NOT NULL,
   `answer` VARCHAR(500) NOT NULL,
   PRIMARY KEY ( `id` )
)CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `ENetTable`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `dataId` INT UNSIGNED,
   `relation` VARCHAR(50) NOT NULL,
   `event` VARCHAR(500) NOT NULL,
   `inference` VARCHAR(500) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `id` )
)CHARSET=utf8;