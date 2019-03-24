CREATE DATABASE flaskcontacts;

USE flaskcontacts;

CREATE TABLE contacts(
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(60),
    phone VARCHAR(60),
    email VARCHAR(60)
)

DESCRIBE contacts;