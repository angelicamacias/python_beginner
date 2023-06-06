import psycopg2

url = "postgres://gxhdoahb:***@horton.db.elephantsql.com/gxhdoahb "
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()

print(first_user)
connection.close()

