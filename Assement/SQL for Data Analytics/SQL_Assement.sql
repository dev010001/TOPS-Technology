create database assement;
use assement;
-- Create the Worker table
CREATE TABLE Worker (
    WORKER_ID INT NOT NULL PRIMARY KEY,
    FIRST_NAME VARCHAR(50),
    LAST_NAME VARCHAR(50),
    SALARY INT,
    JOINING_DATE DATETIME,
    DEPARTMENT VARCHAR(50)
);

-- Insert data from the image
INSERT INTO Worker 
    (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) 
VALUES
    (1, 'Monika', 'Arora', 100000, '2014-02-20 09:00:00', 'HR'),
    (2, 'Niharika', 'Verma', 80000, '2014-06-11 09:00:00', 'Admin'),
    (3, 'Vishal', 'Singhal', 300000, '2014-02-20 09:00:00', 'HR'),
    (4, 'Amitabh', 'Singh', 500000, '2014-02-20 09:00:00', 'Admin'),
    (5, 'Vivek', 'Bhati', 500000, '2014-06-11 09:00:00', 'Admin'),
    (6, 'Vipul', 'Diwan', 200000, '2014-06-11 09:00:00', 'Account'),
    (7, 'Satish', 'Kumar', 75000, '2014-01-20 09:00:00', 'Account'),
    (8, 'Geetika', 'Chauhan', 90000, '2014-04-11 09:00:00', 'Admin');

-- Query to display the output
SELECT * FROM Worker;

-- 1. Order by FIRST_NAME (Asc) and DEPARTMENT (Desc)
SELECT * FROM Worker 
ORDER BY FIRST_NAME ASC, DEPARTMENT DESC;

-- 2. Details for "Vipul" and "Satish"
SELECT * FROM Worker 
WHERE FIRST_NAME IN ('Vipul', 'Satish');

-- 3. FIRST_NAME ends with 'h' and is 6 characters long
SELECT * FROM Worker 
WHERE FIRST_NAME LIKE '_____h';

-- 4. SALARY between 100,000 and 500,000
SELECT * FROM Worker 
WHERE SALARY BETWEEN 100000 AND 500000;

-- 5. Fetch Duplicate Records
SELECT DEPARTMENT, JOINING_DATE, COUNT(*)
FROM Worker
GROUP BY DEPARTMENT, JOINING_DATE
HAVING COUNT(*) > 1;

-- 6. Show top 6 records
SELECT * FROM Worker LIMIT 6;

-- 7. Departments with less than 5 people
SELECT DEPARTMENT, COUNT(WORKER_ID) as 'Number of Workers'
FROM Worker
GROUP BY DEPARTMENT
HAVING COUNT(WORKER_ID) < 5;

-- 8. Departments and count of people
SELECT DEPARTMENT, COUNT(*) AS 'Total_Workers' 
FROM Worker 
GROUP BY DEPARTMENT;

-- 9. Highest salary in each department
SELECT FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT 
FROM Worker 
WHERE (DEPARTMENT, SALARY) IN (
    SELECT DEPARTMENT, MAX(SALARY) 
    FROM Worker 
    GROUP BY DEPARTMENT
);





