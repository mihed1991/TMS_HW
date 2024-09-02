-- SQLite
CREATE TABLE Employees (
Name varchar(100),
Position varchar(100),
Department varchar(100),
Salary int
);
-- -- INSERT INTO Employees VALUES ("Vlad" ,"salesman" ,"sales" ," 2000" ),
-- --                              ("Edgar" ,"salesman" ,"sales" ," 2500" ),
-- --                              ("Misha" ,"salesman", "3000"),
-- --                              ("Liza" ,"Accountant" ,"Accounting" ," 2000" ),
-- --                              ("Sergio" ,"Director" ,"administration" ," 4000" )

-- -- UPDATE Employees SET Position="salesman" WHERE Name="Artem"; 
-- -- ALTER TABLE Employees ADD COLUMN HireDate date;

-- UPDATE Employees SET HireDate="2018-09-03" WHERE Name="Vlad";
-- UPDATE Employees SET HireDate="2020-03-25" WHERE Name="Edgar";
-- UPDATE Employees SET HireDate="2019-06-14" WHERE Name="Misha";
-- UPDATE Employees SET HireDate="2019-12-09" WHERE Name="Liza";
-- UPDATE Employees SET HireDate="2018-01-29" WHERE Name="Sergio";


-- -- SELECT * FROM Employees WHERE Position="salesman";

-- -- SELECT * FROM Employees WHERE Salary > 3000;

-- -- SELECT * FROM Employees WHERE Department="Accountant";

-- -- SELECT AVG(Salary) FROM Employees;

-- -- DROP TABLE Employees
