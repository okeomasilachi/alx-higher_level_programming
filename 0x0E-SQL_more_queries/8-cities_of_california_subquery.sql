-- Find the id of the state named "California"
-- List all the cities of California
SELECT id FROM states WHERE name = 'California';

SELECT * FROM cities WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
) ORDER BY id ASC;
