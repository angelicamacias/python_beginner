import sqlite3

connection = sqlite3.connect("data.db")
#if you wnated to ger a cursor off something like dictionally
connection.row_factory = sqlite3.Row
#Whenever SQlite3 is getting rows form you table it's going to use SQlite row insted of a tuple. 



#create a functio to create a table 
def create_table():
    #commit the transaction that this runs 
    #This is the context manager to automatically commit the changes when we're done. 
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

#insert data
#tell the query what data we want to insert 
def add_entry(entry_content, entry_data): 
    with connection:
        connection.execute(
            f"INSERT INTO entries VALUES (?, ?);", (entry_content, entry_data)
            )


#retrieve data
def get_entries():
    cursor = connection.execute("SELECT * FROM entries);")
    #connection and execute creates the cursor, 
    # uses it to run your query
    #loads the results into the cursor
    return cursor
