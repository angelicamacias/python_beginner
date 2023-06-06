**First stage: One table**

- Users can add movies to a table and store whether they've watched the movie or not 

- We won't support multiple users

**Second stage: two tables**

- We will support multiple users
- In order to do this we need to separate whoe watched what, from the movies themselves 

**Third stage: three tables**

- Finally, we will reduce duplication futher by storing movie information and user information in their own tables 

- The watched table will only reference the other tables 


## Injection attacks


When your programs are coded in such a way that users can execute any SQL code they want, without accessing your database directly 


## Project Features 

Keep track of movies the user is interested in, and their release dates. 



# important


HOW MEANY ENTITIES DO YOU HAVE?

- USERS
- MOVIES

SO.. WE WILL CREATE 2 TABLES

## Autoincreminting IDS

An autoincrementing column means that every time we create a now row, a new unique value is created 


```
SELECT * FROM users JOIN accounts ON users.id = accounts.holder_id;
```

## LIMIT

Maximun number of rows 
We can get the "10 most experienced employees" with ORDER BY and LIMIT

```
SELECT * FROM employees LIMIT 10;
```


## Wildcards

 %f for any number of characters
 _ for one character 


 ## CASCADE constraint

 Witha CASCADE constraint, we cal tell PostgreSQL what to do with an Account when we delete the corresponding User

 ```
 CREATE TABLE accounts(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    account_number TEXT, 
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
 )
```

## What is sensitive data? 


 