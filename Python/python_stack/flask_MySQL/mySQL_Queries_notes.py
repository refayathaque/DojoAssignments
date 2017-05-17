# SQL : Structured Query Language - manages data in relational databases

# SQL Statements :
    # SELECT data
    # SELECT data WHERE some conditions are true
    # INSERT data
    # UPDATE data
    # DELETE data
    # JOIN different tables together

# We will use MAMP along with MySQL Workbench to interact with our database.
# MAMP plays an important role by setting up two different servers -- the web server (called Apache) a
# nd the database server (running MySQL Server).

####

# SELECT

# SELECT * FROM users
# WHERE first_name LIKE "%e" WHERE must always be BEFORE ORDER...
# ORDER BY birthday DESC;

# Exercises : http://sqlzoo.net/wiki/SELECT_names
    # Solutions: https://github.com/Chenzilla/SQL_Zoo/blob/master/1_solution.sql
# Exercises : http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial
    # Solutions: https://github.com/Chenzilla/SQL_Zoo/blob/master/2_solutions.sql

####

# INSERT

# INSERT INTO table_name (column_name1, column_name2)
    # VALUES('column1_value', 'column2_value');

####

# UPDATE

# UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)->(usually id=#)

####

# DELETE

# If you are getting an error regarding SQL SAFE UPDATES, run the following command to let MySQL Workbench know
# that you know what you are doing and you want to DELETE stuff from the database.

# SET SQL_SAFE_UPDATES = 0;

# The SQL command pattern for deleting/removing records is as follows:

# DELETE FROM table_name WHERE condition(s)

# IMPORTANT: if WHERE condition is not added to the DELETE statement, it will delete all the records on the table.

####

# FUNCTIONS

# When calling a function on a column, make sure that column is the appropriate Data Type for that function.

# Text Functions Data Types (VARCHAR, TEXT, CHAR etc.)

# Numeric Functions Data Types (INT, BIGINT, FLOAT etc.)

# Date and Time Functions Data Types (DATETIME)

# SELECT FUNCTION (column) FROM table_name

# Date Format: https://www.w3schools.com/sql/func_date_format.asp

# HAVING THE SEMI COLON IN THE JOIN STATEMENT IS IMPORTANT!!!! JOIN ;;;;;

####

# JOINS

# When using GROUP BY always use some sort of a function

# As mentioned earlier, LEFT JOIN and JOIN are all that you need for web development.

# When SQL uses the keyword JOIN, it only includes those records that have matches on both sides.
# It will omit any records that don't have a 'partner'.

# On the other hand, LEFT JOIN will include all the records from the first table (the 'left' table,
# the first one mentioned when reading from left to right), regardless of whether that record has a
# matching foreign key in the (right) table that we are trying to join to it.

# To summarize, JOIN will only include the intersection of the two tables, whereas LEFT JOIN will include
# all records from the first table, plus the records from the second table that correspond. This is why the
# JOIN is sometimes called the INNER JOIN, while all the other joins (including LEFT JOIN) are referred to as OUTER JOINs.
