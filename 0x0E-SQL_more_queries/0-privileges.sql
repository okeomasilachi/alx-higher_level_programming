-- lists all privileges of the MySQL users
-- user_0d_1 and user_0d_2 on your server
-- (in localhost).
USE mysql;
SELECT * FROM user WHERE User='user_0d_1';
SELECT * FROM user WHERE User='user_0d_2';
