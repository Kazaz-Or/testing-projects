
# comment are lines starting with # or --
-- comment

# Read drom table
SELECT * FROM employees.employees;

# Limit number of rows returned
SELECT * FROM employees.employees LIMIT 99;

# Order the result by id descending order
SELECT * FROM employees.employees ORDER BY id DESC LIMIT 99 ;

# Show only selected columns
SELECT first_name, last_name, email FROM employees.employees ORDER BY id DESC ;

# Read from table matching given criteria ("WHERE" clause)
SELECT first_name, last_name, email, active FROM employees.employees WHERE active = 0;
SELECT * FROM employees.employees WHERE title = 'Sr. Software Engineer' OR title = 'Marketing Intern';

# More example on reading
SELECT * FROM employees.salary;
SELECT * FROM employees.salary WHERE employee_id = 6;
SELECT * FROM employees.salary WHERE salary > 150000 AND created_date >= '2020-07-31 15:28:30';

# get all recrods from post table (wpot_posts) that has post status of 'publish'.
SELECT * FROM demostore13.wpot_posts WHERE post_status = "publish";

# get all recrods from post table (wpot_posts) that has post status of 'publish' also are open for comment(comment_status is open)
SELECT * FROM demostore13.wpot_posts WHERE post_status = "publish" AND comment_status = 'open';

# Multiple conditions
# get all records from post table where post status is published and post_content is empty.
SELECT * FROM demostore13.wpot_posts WHERE post_status = "publish" AND post_content = "";
SELECT * FROM employees.employees WHERE title = 'Sr. Software Engineer' OR title = 'Marketing Intern';

# 'IN' clause. Match condition from list of value
SELECT first_name, title FROM employees.employees WHERE title IN ('Sr. Software Engineer', 'Marketing Intern', 'foo');
SELECT * FROM employees.`employee_contact_information` WHERE city IN ('San Jose', 'Santa Clara', 'Sunnyvale')
AND employee_id > 80; 


# sub query
SELECT GROUP_CONCAT(employee_id) FROM employees.salary WHERE salary >= 150000;
SELECT employee_id FROM employees.salary WHERE salary >= 150000;
SELECT * FROM employees.employees WHERE id IN (18,63,100,49,17,11,87,19,55,86,28,84,94,57,5,2,48,89,16,76,1,46,79,39,71,40,52,64,24,37,65,90,22,15);

SELECT * FROM employees.employees WHERE id 
IN (SELECT employee_id FROM employees.salary WHERE salary >= 150000);

SELECT * FROM employees.employee_contact_information WHERE employee_id 
IN (SELECT employee_id FROM employees.salary WHERE salary >= 100000);

# get records from posts table where post type is 'product' and they have record in 'postmeta' table with 'meta_key='_sale_price'
SELECT * FROM demostore13.wpot_posts WHERE post_type = 'product' AND 
id IN (SELECT post_id FROM demostore13.wpot_postmeta WHERE meta_key = '_sale_price');


# LIKE
SELECT * FROM employees.employees WHERE title LIKE '%Engineer';
SELECT * FROM employees.employees WHERE title LIKE '%Engineer%';
SELECT * FROM employees.employees WHERE title LIKE 'Engineer%';

-- Excericise: find all posts with 'post_title' that are for 'shirt'
SELECT * FROM demostore13.wpot_posts WHERE post_title LIKE '%shirt%';

-- Excercise: find all posts with 'post_title' that has 'hood'
SELECT * FROM demostore13.wpot_posts WHERE post_title LIKE '%hood%';



