CREATE DATABASE youtube_db;
USE youtube_db;

SELECT * FROM top_ug_youtubers_2024

-- CHARINDEX
/*
DATA QUALITY CHECKS, to comfirm this data can be reliable 

1. DATA NEEDS TO BE 100 RECORDS
2. DATA NEEDS TO HAVE 4 FIELDS
3. USERNAME HAS TO BE A STRING FORMAT AND REST IN NUMERIC/FLOAT
4.EACH RECORD SHOULD BE UNQUE, NO DUPLICATES

ROW COUNT =100 (count has 99 dropped 1 entry that had a null value)
COLUMN=4 (initial count had 5 column , dropped extra column)

DATA TYPES
username = varchar
uploads = integer
subs = integer
Video_Views =  integer

Duplicate count = 0 (PASSED)
*/



SELECT COUNT(*) as no_of_rows
FROM top_ug_youtubers_2024;

SELECT COUNT(*) as column_count FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME ='top_ug_youtubers_2024'


-- i get a count of 5 rows so i , when i pull up the table i have an addiation colun called colum1, have to drop this and do the recount,
ALTER TABLE top_ug_youtubers_2024
DROP COLUMN column1;

-- column count
SELECT 
  COLUMN_NAME,
  DATA_TYPE
FROM
  INFORMATION_SCHEMA.COLUMNS
WHERE
  TABLE_NAME ='top_ug_youtubers_2024'

-- changing data types from float to int/bigint
ALTER TABLE top_ug_youtubers_2024
ALTER COLUMN Video_Views BIGINT;

-- dupicate check/count

SELECT 
  Username,
  COUNT(*) as duplicate_Count
FROM 
  top_ug_youtubers_2024
GROUP BY
  Username
HAVING 
  COUNT(*) > 1;







