######### Special Functions  #################

# COUNT

SELECT * FROM employees.employees;
SELECT COUNT(*) FROM employees.employees;
SELECT COUNT(*) FROM employees.employees WHERE active = 1;
SELECT COUNT(*) FROM employees.employees WHERE active = 0;
SELECT COUNT(*) FROM employees.employees WHERE title = 'Sr. Software Engineer';

# MAX/MIN
SELECT MAX(salary) FROM employees.salary;
SELECT MIN(salary) FROM employees.salary;
SELECT SUM(salary) FROM employees.salary;

# DISTINCT
SELECT * FROM employees.employees;
SELECT DISTINCT(title) FROM employees.employees;
SELECT DISTINCT(post_type) FROM demostore13.wpot_posts;

# GROUP BY
SELECT title, COUNT(*) FROM employees.employees GROUP BY title;
SELECT post_type, COUNT(*) FROM demostore13.wpot_posts GROUP BY post_type;

# CONCAT
SELECT 
CONCAT('insert into employees.employees where  (first_name, last_name) values (', first_name, ' ', last_name, ');') 
FROM employees.employees;


