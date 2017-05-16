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
