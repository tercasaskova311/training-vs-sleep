CREATE TABLE new_schema1.training_data AS SELECT * FROM bakery.training_data;
RENAME TABLE new_schema1.cleaned_and_standardized_sleep_data TO new_schema1.sleep_data;

SELECT * 
FROM new_schema1.training_data ;

SELECT Date 
FROM new_schema1.sleep_data;

#Select statement to display the formatted date

SELECT DATE_FORMAT(STR_TO_DATE(Date, '%d.%m.%Y'), '%Y-%d-%m') AS formatted_date
FROM new_schema1.sleep_data;

#Update statement to change the date format in the table
SET SQL_SAFE_UPDATES = 0;

UPDATE new_schema1.sleep_data
SET Date = DATE_FORMAT(STR_TO_DATE(Date, '%d.%m.%Y'),'%d-%m-%Y');

SELECT DATE_FORMAT(STR_TO_DATE(WorkoutDay, '%Y-%m-%d'),'%d-%m-%Y') AS formatted_date
FROM new_schema1.training_data;
   
UPDATE new_schema1.training_data
SET WorkoutDay = DATE_FORMAT(STR_TO_DATE(WorkoutDay, '%Y-%m-%d'),'%d-%m-%Y');


#join training data and sleep to compare hours on bike in relation to sleep.

SELECT WorkoutDay, Date  AS date
FROM new_schema1.training_data t1, new_schema1.sleep_data
LEFT JOIN
    new_schema1.sleep_data t2 ON t1.WorkoutDay = t2.Date;
    
#creating new table
CREATE TABLE new_schema1.sleep_vs_training AS 
	SELECT
		t2.Date,
		t1.WorkoutDay,
		t2.sleep,
		t2.`Sleep performance %`,
		t2.`Deep (SWS) duration (min)`,
		t1.WorkoutType,
		t1.Time,
		t1.HRZone4,
		t1.HRZone5,
		t1.TSS
FROM new_schema1.training_data t1
LEFT JOIN new_schema1.sleep_data t2 ON t1.WorkoutDay = t2.Date;
    
SELECT * FROM new_schema1.sleep_vs_training 

ALTER TABLE new_schema1.sleep_vs_training
DROP COLUMN WorkoutDay;

DELETE FROM new_schema1.sleep_vs_training
WHERE Date IS NULL OR Sleep IS NULL;

CREATE TABLE new_schema1.sleep_vs_training2 AS
SELECT * FROM new_schema1.sleep_vs_training3;

ALTER TABLE new_schema1.sleep_vs_training
DROP COLUMN HRZone4;

ALTER TABLE new_schema1.sleep_vs_training
DROP COLUMN HRZone5;

DELETE FROM new_schema1.sleep_vs_training
WHERE Time = '00:00:00';


#duplicates - Create a temporary table to store the IDs of the duplicate rows
CREATE TEMPORARY TABLE temp_duplicates AS
SELECT Date
FROM new_schema1.sleep_vs_training 
WHERE Date IN (
    SELECT Date
    FROM new_schema1.sleep_vs_training 
    GROUP BY Date
    HAVING COUNT(date) > 1
)
AND Date NOT IN (
    SELECT MIN(Date)
    FROM new_schema1.sleep_vs_training 
    GROUP BY date
    HAVING COUNT(date) > 1
);
SELECT * FROM temp_duplicates;

#Update the duplicate cells to NULL
UPDATE my_table
SET date = NULL
WHERE id IN (SELECT id FROM temp_duplicates);

#Drop the temporary table
DROP TEMPORARY TABLE temp_duplicates;

