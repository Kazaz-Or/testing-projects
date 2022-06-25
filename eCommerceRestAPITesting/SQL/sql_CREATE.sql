# Demo of `CREATE TABLE` query
create database foobar2;
DROP DATABASE `foobar2`;

# Create copy of a table
create table foobar.new_employees like employees.employees ;
create table employees.employees2 like employees.employees ;

# Insert data from one table to another table
insert into employees.employees2 select * from employees.employees;

# verify data in the new table
select * from employees.employees2;

# Completely delete (destroy) table
DROP TABLE `employees`.`employees2`;

# Delete all data in the given table
TRUNCATE `employees`.`employees2`;