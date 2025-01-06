-- Department Top Three Salaries

# Write your MySQL query statement below

WITH
  EmployeesWithRank AS (
    SELECT
      Department.name AS department,
      Employee.name AS employee,
      Employee.salary,
      DENSE_RANK() OVER(
        PARTITION BY Employee.departmentId
        ORDER BY Employee.salary DESC
      ) AS `rank`
    FROM Department
    INNER JOIN Employee
      ON (Department.id = Employee.departmentId )
  )
SELECT
  department AS Department,
  employee AS Employee,
  salary AS Salary
FROM EmployeesWithRank
WHERE `rank` <= 3;