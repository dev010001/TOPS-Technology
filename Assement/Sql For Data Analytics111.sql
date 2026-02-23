create database try;
USE try;

create table employee (
	Employee_id int auto_increment PRIMARY KEY,
    Name varchar(100),
    position varchar(100),
    Salary decimal(10, 2),
    Hire_date date
);

Create table employee_audit (
	Audit_id int auto_increment primary key,
    employee_id int,
    Name varchar(100),
	Position VARCHAR(100),
    salary DECIMAL(10, 2),
    hire_date DATE,
    action_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

insert into employee (Name, position, salary, hire_date) values
('John Doe', 'Software Engineer', 80000.00, '2022-01-15'),
('Jane Smith', 'Project Manager', 90000.00, '2021-05-22'),
('Alice Johnson', 'UX Designer', 75000.00, '2023-03-01');

DELIMITER $$

Create trigger aafter_employee_insert
after insert on employee
for each row
begin
	insert into employee_audit (
		employee_id,
        Name,
        Position,
        salary,
        hire_date
    )
    values (
		NEW.Employee_id,
        NEW.Name,
        NEW.Position,
        NEW.salary,
        NEW.hire_date
    );

END$$

DELIMITER ;

DELIMITER $$

Create procedure add_employee(
	IN emp_name varchar(100),
    IN emp_position varchar(100),
    IN emp_salary decimal(10,2),
    IN emp_hire_date date
    )
BEGIN
	insert into employee (Name, Position, Salary, Hire_date)
    values (emp_name, emp_position, emp_salary, emp_hire_date);
END$$

DELIMITER ;

CALL add_employee(
	'Michael Brown',
    'Data Analyst',
     70000.00,
    '2024-02-10'
);

select * from employee;
select * from employee_audit;
