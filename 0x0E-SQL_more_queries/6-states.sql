-- Create database hbtn_0d_usa if it doesn't exist
-- Create table states if it doesn't exist
-- Use the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
