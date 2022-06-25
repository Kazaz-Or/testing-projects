SELECT * FROM employees.employees;
SELECT * FROM employees.salary;

# Get records from 2 tables that is in common between the two
SELECT * FROM employees.employees JOIN employees.salary
ON employees.id = salary.employee_id;
SELECT * FROM employees.employees INNER JOIN employees.salary
ON employees.id = salary.employee_id;

# Use aleas when joining tables
SELECT * FROM employees.employees e JOIN employees.salary s
ON e.id = s.employee_id;

# Get only specific columns (fields)
SELECT e.first_name, e.last_name FROM employees.employees e JOIN employees.salary s
ON e.id = s.employee_id;

# Display records only from one of the joined tables
SELECT e.* FROM employees.employees e JOIN employees.salary s
ON e.id = s.employee_id where s.salary > 150000;

# Join 3 tables
SELECT * FROM employees.employees e JOIN employees.salary s ON e.id = s.employee_id
JOIN employees.employee_contact_information c on e.id = c.employee_id
 where s.salary > 150000;
 
# Display only selected columns
SELECT e.first_name, e.last_name, c.phone_number FROM employees.employees e JOIN employees.salary s ON e.id = s.employee_id
JOIN employees.employee_contact_information c on e.id = c.employee_id
 where s.salary > 150000;

# LEFT JOIN - Get records that are missing in the second table
select * from employees.employees;
select * from employees.employee_contact_information;
select * from employees.employees e left join employees.employee_contact_information c
on e.id = c.employee_id where c.employee_id is null;

-- Excercise: get list of users that do not have any posts
select * from demostore13.wpot_users u left join demostore13.wpot_posts p
on u.id = p.post_author WHERE p.id is null;









