User presses 1 
~We ark them for date and contents of the entry 
~We'll use two separate prompts 

--> Viewing entries
~If the user presses 2 in the menu, we'll show them their entries. 

~For each entry, we show data and content 

--> Selectiong new otions 
~After the user makes a selection and we perform the appropriate action, they can choose another. 

~We'll continually ask until they enter 3 to exit. 


## What is SQL? 
Qtructure dQuery Langues 
Uses to interact with relational database Management systems(RDBMS)
SQL ins meant to be similar to english 

### Relation databases 
Large, complex and poweful. Examples include PosrgreSQL, MySQL or SQLite 
Databases are constructed primarily form tables. Tables have columns, and zero or more rows. 

## Why "Relational"? 

To do with how tables are used together.
You can see how these two tables are related.
To simplify relations, we often use unique identifiers
But now we no loger need the holder column! 

## Using python lists as an in-memory databases 
 
## A SQLite data viewer 

### CREATE TABLE

- CREATE TABLE accounts (name TEXT, number TEXT);

    - A semicolon to sinal the end of the query 
    - SQLite has 5 mejor types: 
        - Integer 
        - Text
        - Blob 
        - Real 
        - Numberic 

- CREATE TABLE IF NOT EXISTS accounts (name TEXT, number TEXT); 

## COMMENTS in SQL 
Something you may want to do every now and then, especially as we write longer queries, is add comments.

A comment is something that won't run, but you can read later on. They can be very useful for yourself (if you come back to a query after a few days or weeks), but also for anyone else reading your queries.

To write a comment in SQLite, we precede the text with two dashes, like this:
```
-- This is a comment.
-- The line below is not a comment.
CREATE TABLE users (first_name TEXT, surname TEXT);
```
================================ EXERCISE =========================== 
--> Exercise 1
Create a table for storing books in your book list. The table should be able to contain the book's title, the author, and the date of publication as a string.
 - SOLUTION 
```
 CREATE TABLE "Book's " (
	"Author"	TEXT,
	"Date"	TEXT
);
```

--> Exercise 2
Create a table for storing information about a person that writes book reviews. For each person, store their name, their location as a string, and how many book reviews they have written.
- SOLUTION 
```
CREATE TABLE "Book reviews" (
	"Name"	TEXT,
	"Location "	TEXT,
	"No_book_reviews"	INTEGER
);
```

--> Exercise 3
Create a table for storing temperature readings of a thermometer inside a greenhouse. Each reading should contain the temperature as well as the date and time of the reading, as a string.
- SOLUTION 
```
CREATE TABLE "Temperature" (
	"Temperature"	REAL,
	"Date"	TEXT
);
```

## How to connnect to a SQLite database eith pyhon 
- First import the module
- Then use it to connect to the data file 
    - If the data file dosen't already exist when you try to connect, this will create one. 
-When connected, you can execute SQL queries. 

```
import sqlite3

connection = sqlite3.connect("data.db")
connection.execute("CREATE TABLE entries (content TEXT, data TEXT);")
connection.close()
```
- Open a cnnection with sqlite3.connect()
- Use the connection to execute queries
- At the end, always close the connection

## Creating a function for connecting 
- Normally i would create the connection in a funciton
- Often, we delete and re-create the data file, so having an easy-to-call function that creates the data file is convenient.  

``` 
import sqlite3

def create_table():
    connection = sqlite3.connect("data.db")
    connection.execute("CREATE TABLE entries (content TEXT, data TEXT);")
    connection.close()
```
NOTE: How many connections can you open? 
- You can open as many as you want 
- But only one connection can write to the databases at a time 

If you have two connecions one of them can be inserting new data into the database, the other one to insert data into the database at the same time it has to wait until the other one has finshed. 

- Therefore, for single-user applications (like console apps), having a single connection si enough. 

## Creating one connection only
-Instead of a function that creates the connection, we can create the connection at the top of the file. 
- Then we can use it in the functions below 

```
connnection = sqlite3.connect("data.db)

def creat_table():
    connection.execute("CREATE TABLE entries (content TEXT, data TEXT);)

def colse_connection():
    connection.close()
```

## What are transaction? 

- We can run multiple queries in a transaction.
- Queries run in order in which they're executed, but all queries in a transaction must succeed, or none will. There have to be no errors or anything like that, if not, then all the queries in the transacion will be cancelled. 
- Therefore, transactions allow us to group realted queries so we're sure they all happen together successfully.

## Commit and rollback 

- Transactions can either be committed or rolled back. 
- Committing sabes the database changes permanently, so they'll be available to read later. 
- Rolling back undoes the changes, as if nothing happend in the transaction.

## Are we using transactions? 

- Every time we call connecition.esecute(), a transaction is created. 
- But we haven't been committing or rolling back. 
- You'll see that if you execute any of the code shown earlier, and then open the database, the changes won't be there. 


we can do connections.commit() after executing a query

```
def create_table(): 
    connection.execute("CREATE TABLE entries (content TEXT, data TEXXT);")
    connection.commit()
```
 we can use a context manager to handle auntomatically committing at the end. 

 ```
 def create_table():
    with connection: 
        connetction.execute("CREATE TABLE entries (contect TEXT, data TEXT);")
```
## How to connect to a SQLite database with python
- First import the module
- Then use it to connect to the data file 
    - If the data file dosen't already exist when you try to connect, this will create one. 
- When connected, you can execute SQL queries 
```
import sqlite3

connection = sqlite3.connect("data.db")
connection.execute("CREATE TABLE entries (conect TEXT, date TEXT);")
connextion.close()
```
        -Open a connection with sqlite2.connect()
        -Use the connection to execute queries
        -At the end, always close the connection

## Creating a function for connecting 

- NOrmally i would create the connection in a function 
- Often, we delete and re-create the data file, so habing an easy-to-call function that creates the data file is convenient
```
import sqlite3

def creat_table()
    conneciton = sqlite3.connect("data.db")
    connection.execute("CREATE TABLE entries (conect TEXT, data TEXT);")
    connection.close()
```


## How many connections can you open? 
- You can open as many as you want
- But on ly one connection can write to the database at a time
- Therefore, for single-user application (like console apps), having a single connection is enough 

## Creating one conecction only 

- Instead fo a function that creates the connection, we can creae the connection at the tops of the file 
- Then we can use it in the functions below

```
connection = sqlite3.connect("data.db")

def create_table():
    connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")

def close_connection():
    connection.close()
```

## What are transaction? 

- We can run multiple queris in a transaction 
- Queries run in order in which they're executed, but
- All queries in a transaction must succed, or none will
- Therefore, transactions allow us to group related queries so we're suer they all happen together successfully 

## Commit and rollback 

- Transactions can either be committed or rolled back.
- Committing saves the database changes permanently, so they'll be available to read later. 
- Rolling back undoes the changes, as if nothing happend in the transaction. 

## Are we using transactions? 

- Every time we call connection.execute(), a transaction is created. 
- But we haven't veen committing or rolling back.
- You'll see that if you execute any of the code shown earlier, and then open the database, the changes won't be there. 

## Two ways to commit 

- We can do connection.commit() after executing a query
```
def create_table():
    connection.execute("CREATE TABLE entries (content TEXT, data TEXT);")
    connection.commit()
```
- We can use a contect manager to handle automatically committing at the end

```
def create_table():
    with connection:
        connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")

```
## How to connect to a SQLite database eith python 


## What is a cursor? 
- A strucute that allows us to traverse a result set. 
- Database cursors allow the database to only load results when requested. 
- SQLite cursors load all results, but help us go over them more easily. 


NOTA: 

.cursor()
Return a new Cursor Object using the connection.

### Iterating over cursors 

- SQLite cursors represent that ponte we saw earlier. 
- They help us iterate over the results. 
- Therefore using them in for loops like this makes some sense. 

```
connection = sqlite3.sonnect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")

for row in cursor: 
    print(row)

connection.close()
```
### When not interating over cursors 

If we don't use cursors for interation, then SQLite cursors seem pointless 

```
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("ISERT INTO users ('John Smith', 35);')
connection.close()
```

### SQLite shorhand for creating cursors

- With sqlite3, connection.execute() creates a cursor for us
- This saves us some typing and makes amore sense when doing things like inserting 

```
def create_table(): 
    connection = sqlite3.connect("data.db")
    cursor.execute("CREATE TALBE entries (content TEXT, date TEXT);")
    connection.close()
```
## INSERT INTO: add data into a table
example
```
INSERT INTO users (first_name, surname) VALUES ('Rolf', 'Smith');
```
INSERT INTO users: This talls the database we want to add data to the users table. 
(first_name, surname): These are the solumns that we want to add data to. This is optional, in which case we'll insert into all columns. 

VALUES ('Rolf', 'Smith'): We tell the database what values we want to insert in those columns. 
Remember if we skipped the columns, we'll need to provide values for all columns.


=========================================== EXERCISE =========================================
Exercise 1
Given this table:

CREATE TABLE users (id INTEGER, first_name TEXT, surname TEXT, salary INTEGER);
Insert 3 rows. Each row should have different unique id value, starting at 1 and increasing by 1 each time. Make up the other values, but make sure to use the correct type of data!

SOLUTION
INSERT INTO users VALUES ('1', 'Billy', 'Martinez', '98736');
INSERT INTO users VALUES ('3', 'Blanquit', 'Martinez', '98736');
INSERT INTO users VALUES ('3', 'Gris', 'Martinez', '98736');

Exercise 2
Given this table:

CREATE TABLE entries (content TEXT, publication_date TEXT);
Insert 2 rows with a different publication date. You can choose whatever format for the date you want, but be consistent! That's one of the most important things when working with databases.

SOLUTION
INSERT INTO entries VALUES ('CATS', '12-2-2009');
INSERT INTO entries VALUES ('DOGS', '12-8-2010');


## HOW TO INSERT DATA INTO SQLITE WITH PYTHON

## SELECT: retrieve data form a table 

```
SELECT first_name, surname FROM users;
```
SELECT: This tells the database we want to find and retrieve data. 
first_name: Here we say what columns we want to retrieve data from. 
FROM users: And finally, what table we want to retrieve data from. 

### SELECT
- Filtering the selected data so we only get rows with certain values
    - Use the WHERE clause. 
- SELECT data from multiple tables at one 
    - Use JOIN 

## WHERE: search with SQL 

SELECT * FROM users
    WHERE first_name = 'Jhon';
    WHERE age > 18;
    WHERE salary < 52000;
    WHERE surname != 'Smith';


## DROP TABLE: deleting entire tables

```
DROP TABLE entries;
```
DROP TABLE: This tells the database we want to delete the entire table as if it never existed. 

entries: This is the table we want to delete. 

```
DROP TABLE IF EXISTS entries;
```
IF EXISTS: if exists can be used to prevent a database error if the table dosen't exist. 

## What is a SQL injection attack? 

SQL injection attack: When your programs are coded in such a way that users can execiute any SQL code they want, without accessing your database directly. 

sql
```
SELECT * FROM users WHERE first_name = ?;
```
python
```
GET_USER = "SELECT * FROM user WHERE first_name = {};"
```

```
cursor.exxecute(GET_USER.FORMAT(USERNAME))
```

```
Welcom to the username searching app!
Enter you username: ''; DROP TABLE users;
```

Don't fall for this!

Your python code would now be running this: 
     SELECT * FROM user WHERE first_name = ''; DROP TABLE user; 
Use ? instead of string formatting when working with databases. 
This would've saved you: 
    GET_USER  = "SELECT * FROM users WHERE first_name = ?;"
    cursor.execute(GET_USER, (username, ))

# PROJECT 2
### OVERVIEW OF THE PROJECT

-Keep track of movies the user is interested in, and their release dates. 
-Store which mobies the user has alredy watched. 
-Add new users to leep track of their watched movies separately. 


## Starting code for this project 