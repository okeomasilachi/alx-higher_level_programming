-- List all cities with their IDs, names,
-- and the corresponding state names
SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
