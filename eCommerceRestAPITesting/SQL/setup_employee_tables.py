

import pymysql
import random
import string




class SetupEmployeeDemoTables(object):


    first_names = ['Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen', 'Nancy',
     'Margaret', 'Lisa', 'Betty', 'Dorothy', 'Sandra', 'Ashley', 'Kimberly', 'Donna', 'Emily', 'Michelle', 'Carol',
     'Amanda', 'Melissa', 'Deborah', 'Stephanie', 'Rebecca', 'Laura', 'Sharon', 'Cynthia', 'Kathleen', 'Helen', 'Amy',
     'Shirley', 'Angela', 'Anna', 'Brenda', 'Pamela', 'Nicole', 'Ruth', 'Katherine', 'Samantha', 'Christine', 'Emma',
     'Catherine', 'Debra', 'Virginia', 'Rachel', 'Carolyn', 'Janet', 'Maria', 'Heather', 'Diane', 'Julie', 'Joyce',
     'Victoria', 'Kelly', 'Christina', 'Joan', 'Evelyn', 'Lauren', 'Judith', 'Olivia', 'Frances', 'Martha', 'Cheryl',
     'Megan', 'Andrea', 'Hannah', 'Jacqueline', 'Ann', 'Jean', 'Alice', 'Kathryn', 'Gloria', 'Teresa', 'Doris', 'Sara',
     'Janice', 'Julia', 'Marie', 'Madison', 'Grace', 'Judy', 'Theresa', 'Beverly', 'Denise', 'Marilyn', 'Amber',
     'Danielle', 'Abigail', 'Brittany', 'Rose', 'Diana', 'Natalie', 'Sophia', 'Alexis', 'Lori', 'Kayla', 'Jane'
     'James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Christopher',
     'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew', 'Kenneth', 'Joshua', 'George',
     'Kevin', 'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan', 'Jacob', 'Gary', 'Nicholas', 'Eric',
     'Stephen', 'Jonathan', 'Larry', 'Justin', 'Scott', 'Brandon', 'Frank', 'Benjamin', 'Gregory', 'Samuel', 'Raymond',
     'Patrick', 'Alexander', 'Jack', 'Dennis', 'Jerry', 'Tyler', 'Aaron', 'Jose', 'Henry', 'Douglas', 'Adam', 'Peter',
     'Nathan', 'Zachary', 'Walter', 'Kyle', 'Harold', 'Carl', 'Jeremy', 'Keith', 'Roger', 'Gerald', 'Ethan', 'Arthur',
     'Terry', 'Christian', 'Sean', 'Lawrence', 'Austin', 'Joe', 'Noah', 'Jesse', 'Albert', 'Bryan', 'Billy', 'Bruce',
     'Willie', 'Jordan', 'Dylan', 'Alan', 'Ralph', 'Gabriel', 'Roy', 'Juan', 'Wayne', 'Eugene', 'Logan', 'Randy',
     'Louis', 'Russell', 'Vincent', 'Philip', 'Bobby', 'Johnny', 'Bradley']

    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson',
                  'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson',
                  'White', 'Lopez', 'Lee', 'Gonzalez', 'Harris', 'Clark', 'Lewis', 'Robinson', 'Walker', 'Perez',
                  'Hall', 'Young', 'Allen', 'Sanchez', 'Wright', 'King', 'Scott', 'Green', 'Baker', 'Adams', 'Nelson',
                  'Hill', 'Ramirez', 'Campbell', 'Mitchell', 'Roberts', 'Carter', 'Phillips', 'Evans', 'Turner',
                  'Torres', 'Parker', 'Collins', 'Edwards', 'Stewart', 'Flores', 'Morris', 'Nguyen', 'Murphy', 'Rivera',
                  'Cook', 'Rogers', 'Morgan', 'Peterson', 'Cooper', 'Reed', 'Bailey', 'Bell', 'Gomez', 'Kelly',
                  'Howard', 'Ward', 'Cox', 'Diaz', 'Richardson', 'Wood', 'Watson', 'Brooks', 'Bennett', 'Gray',
                  'James', 'Reyes', 'Cruz', 'Hughes', 'Price', 'Myers', 'Long', 'Foster', 'Sanders', 'Ross',
                  'Morales', 'Powell', 'Sullivan', 'Russell', 'Ortiz', 'Jenkins', 'Gutierrez', 'Perry', 'Butler',
                  'Barnes', 'Fisher']

    titles = ['Sr. Software Engineer', 'Jr. Software Engineer', 'Dev Ops', 'Marketing Intern', 'Human Resources Admin', 'Engineering Manager']
    cities = ['San Francisco', 'San Jose', 'Santa Clara', 'Mountain View', 'Sunnyvale', 'Palo Alto', 'San Mateo', 'Daily City']


    def __init__(self, drop_db_if_exist):
        self.drop_db_if_exist = drop_db_if_exist
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.password = 'mysql'
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, autocommit=True, db=None)

    @staticmethod
    def generate_random_email_address():
        letters = string.ascii_lowercase
        result_str = ''.join(random.sample(letters, 10))
        return result_str + random.choice(['@gmail.com', '@yahoo.com', '@comcast.net'])

    @staticmethod
    def generate_random_phone_number():
        return '1' + ''.join(random.sample(string.digits, 10))

    @staticmethod
    def generate_random_address():
        rand_number = ''.join(random.sample(string.digits, random.randint(1, 5)))
        rand_string = ''.join(random.sample(string.ascii_lowercase, 10))
        rand_address = rand_number + ' ' + rand_string + ' ' + random.choice(['St', 'Ave', 'Blvd'])
        return rand_address

    def create_db_connection(self):
        return pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, autocommit=True, db=None)

    def create_employees_database(self):
        sql = "CREATE DATABASE employees;"
        try:
            connection = self.create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(sql)
        finally:
            connection.close()

    def drop_employees_database(self):
        sql = "DROP DATABASE IF EXISTS employees;"
        try:
            connection = self.create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(sql)
        finally:
            connection.close()

    def create_employees_table(self):

        sql = """CREATE TABLE `employees`.`employees` (
                  `id` int(11) NOT NULL AUTO_INCREMENT,
                  `first_name` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
                  `last_name` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
                  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
                  `title` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
                  `active` int(11) NOT NULL,
                  `modified_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                  `created_date` timestamp NOT NULL,
                  PRIMARY KEY (`id`),
                  UNIQUE KEY `email_UNIQUE` (`email`));"""
        try:
            connection = self.create_db_connection()
            print("Executing SQL: \n {}".format(sql))
            with connection.cursor() as cursor:
                cursor.execute(sql)
        finally:
            connection.close()

    def create_records_in_employees_table(self):
        try:
            connection = self.create_db_connection()
            random.shuffle(SetupEmployeeDemoTables.first_names)
            random.shuffle(SetupEmployeeDemoTables.last_names)

            for f_name in SetupEmployeeDemoTables.first_names:
                if SetupEmployeeDemoTables.last_names:
                    l_name = SetupEmployeeDemoTables.last_names.pop()
                    email = f_name[0] + l_name + '@supersqa.com'
                    sql = f"""INSERT INTO `employees`.`employees` (`first_name`, `last_name`, `email`, `title`, `active`, `created_date`)
                            VALUES ('{f_name}', '{l_name}', '{email.lower()}', '{random.choice(SetupEmployeeDemoTables.titles)}', '{random.choice([0,1])}', now());"""
                    print("Executing SQL: \n {}".format(sql))
                    with connection.cursor() as cursor:

                        cursor.execute(sql)
        finally:
            connection.close()

    def create_salary_table(self):
        sql = """CREATE TABLE `employees`.`salary` (
                  `id` INT NOT NULL AUTO_INCREMENT,
                  `employee_id` VARCHAR(45) NOT NULL,
                  `salary` DECIMAL(7,0) NOT NULL,
                  `created_date` TIMESTAMP NOT NULL,
                  `modified_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                  PRIMARY KEY (`id`, `employee_id`),
                  UNIQUE INDEX `employee_id_UNIQUE` (`employee_id` ASC) VISIBLE);"""

        try:
            connection = self.create_db_connection()
            print("Executing SQL: \n {}".format(sql))
            with connection.cursor() as cursor:
                cursor.execute(sql)
        finally:
            connection.close()

    def get_all_employees_from_employees_table(self):
        sql = "SELECT * FROM employees.employees;"
        try:
            connection = self.create_db_connection()
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                all_rows = cursor.fetchall()
        finally:
            connection.close()

        return all_rows

    def create_records_in_salary_table(self, list_of_employees):

        min_salary = 80000
        max_salary = 200000

        # randomize the employees so the id of the table is not exactly same as id of employee (just visually better and
        # easier for new students to understand they are not the same ids
        random.shuffle(list_of_employees)
        for employee in list_of_employees:
            employee_id = employee['id']
            insert_sql = f"""INSERT INTO `employees`.`salary` (`employee_id`, `salary`, `created_date`)
                            VALUES ({employee_id}, {random.choice(range(min_salary, max_salary))}, now());"""
            try:
                connection = self.create_db_connection()
                print("Executing SQL: \n {}".format(insert_sql))
                with connection.cursor() as cursor:
                    cursor.execute(insert_sql)
            finally:
                connection.close()

    def create_employee_contact_information_table(self):
        sql = """CREATE TABLE `employees`.`employee_contact_information` (
                  `id` INT NOT NULL AUTO_INCREMENT,
                  `employee_id` VARCHAR(45) NOT NULL,
                  `personal_email` VARCHAR(100) NOT NULL,
                  `phone_number` VARCHAR(20) NOT NULL,
                  `address_line_1` VARCHAR(100) NULL,
                  `address_line_2` VARCHAR(100) NULL,
                  `city` VARCHAR(45) NULL,
                  `state` VARCHAR(2) NULL,
                  `zip_code` VARCHAR(10) NULL,
                  `country` VARCHAR(45) NULL,
                  `created_date` TIMESTAMP NOT NULL,
                  `modified_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                  PRIMARY KEY (`id`, `employee_id`),
                  UNIQUE INDEX `employee_id_UNIQUE` (`employee_id` ASC) VISIBLE);
                """
        try:
            connection = self.create_db_connection()
            print("Executing SQL: \n {}".format(sql))
            with connection.cursor() as cursor:
                cursor.execute(sql)
        finally:
            connection.close()

    def create_records_in_employee_contact_information_table(self, list_of_employees):

        # randomize the employees so the id of the table is not exactly same as id of employee (just visually better and
        # easier for new students to understand they are not the same ids
        random.shuffle(list_of_employees)
        for employee in list_of_employees:
            employee_id = employee['id']

            insert_sql = f"""INSERT INTO `employees`.`employee_contact_information` (`employee_id`, `personal_email`, 
                    `phone_number`, `address_line_1`, `address_line_2`, `city`, `state`, `zip_code`, `country`, 
                    `created_date`)
                    VALUES ({employee_id}, '{self.generate_random_email_address()}', '{self.generate_random_phone_number()}',
                    '{self.generate_random_address()}', NULL, '{random.choice(SetupEmployeeDemoTables.cities)}',
                        'CA', {''.join(random.sample(string.digits, 5))}, 'USA', now());"""

            try:
                connection = self.create_db_connection()
                print("Executing SQL: \n {}".format(insert_sql))
                with connection.cursor() as cursor:
                    cursor.execute(insert_sql)
            finally:
                connection.close()

    def main(self):

        # if 'drop_db_if_exist' is set to true the existing database is droped and new one created
        if self.drop_db_if_exist:
            self.drop_employees_database()

        # first create the database
        self.create_employees_database()

        # then create the employees table
        self.create_employees_table()

        # populate employees
        self.create_records_in_employees_table()

        # create the salary table
        self.create_salary_table()

        # for each of the existing employees, add salary data
        all_employees = self.get_all_employees_from_employees_table()
        self.create_records_in_salary_table(all_employees)

        # create the table to store contact information for employees
        self.create_employee_contact_information_table()

        # populate employee contact info
        self.create_records_in_employee_contact_information_table(all_employees)

if __name__ == '__main__':

    obj = SetupEmployeeDemoTables(drop_db_if_exist=True)
    obj.main()