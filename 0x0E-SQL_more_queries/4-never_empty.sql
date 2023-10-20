-- Check if the table id_not_null exists
-- Create the table id_not_null
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
