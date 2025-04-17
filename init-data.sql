USE master;
GO

-- Create a new test database
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'TestDB')
BEGIN
    CREATE DATABASE TestDB;
END
GO

USE TestDB;
GO

-- Drop table if it exists
IF OBJECT_ID('dbo.AdditionTests', 'U') IS NOT NULL
    DROP TABLE dbo.AdditionTests;
GO

-- Create a table for test cases
CREATE TABLE dbo.AdditionTests (
    id INT PRIMARY KEY,
    a INT,
    b INT,
    c INT,
    expected_result BIT
);
GO

-- Insert test records
INSERT INTO dbo.AdditionTests (id, a, b, c, expected_result) VALUES
-- Passing cases
(1, 1, 2, 3, 1),
(2, -1, -1, -2, 1),
(3, 0, 0, 0, 1),
(4, 1000, 2000, 3000, 1),
(5, -10, 10, 0, 1),

-- Failing cases
(6, 1, 2, 4, 0),
(7, -1, -1, -3, 0),
(8, 0, 0, 1, 0),
(9, 1000, 2000, 4000, 0),
(10, -10, 10, 5, 0);
GO