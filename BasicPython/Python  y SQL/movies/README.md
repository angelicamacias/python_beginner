# Movie watchlist

Application to keep track of a movie database and the movies that have watched. 

## User interfase 

- Welcome messages 
- User menu 

### Menu 

- Adding movie: The user will enter the date in the correct format: "dd-mm-YYYY"
- Viewing upcoming movies: Show movies just are after to day 
- Viewing all movies
- Adding a watched movie for a user
- Viewing a user's watched movies
- Adding a user

## Database 

we'll be using a cloud PostgreSQL provider, the free vertion.
https://www.elephantsql.com
we will need the URL to access the database using Python

The database.py file contains SQL queries and functions for interacting with the PostgreSQL database

## Connection with Database

Our program is coded to expect an environment variable, that we will define with their database connection string.

It reads it, and connects to whatever connection string is provided

### Create a environment variable

Create a text file called **.env** where we store environment variables
When we run the program, we tell the operating system to turn the contents of that file into environment variables 

NOTE: We'll use a library called python-dotenv for this 

- Create the .env and .env .exmaple files
- Install python-dotenv
- Load the environment variables whene we start the app
- Use the environment variable value as our connection string. 

image.png