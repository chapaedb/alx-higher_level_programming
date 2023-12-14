-- Prints name and scores ignoring where name is null
SELECT score, name
WHERE name IS NOT NULL
FROM second_table
ORDER BY score Desc;
