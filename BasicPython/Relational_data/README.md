Exercise
For this exercise I've created a db fiddle that sets up a departments table for you:

| id INTEGER PRIMARY KEY | name TEXT | department_lead TEXT |
| ---------------------- | --------- | -------------------- |


Create another table for employees that references the one I've created.

The new table should have these columns:

id, which should be a primary key.

first_name.

surname.

department_id, which should be a foreign key to the departments.id column.



Solution


CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    surname TEXT,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

