import os 
import psycopg2
from dotenv import load_dotenv


load_dotenv()

SELECT_POLLS = "SELECT * FROM polls;"
SELECT_OPTIONS_IN_POLL= """
SELECT options.option_text, SUM(votes.options_id) FROM options
JOIN polls ON options.poll_id = polls.id
JOIN votes ON options.id = votes.options_id
WHERE polls.id = %s
GROUP BY options.option_txt;
"""

connection = psycopg2.connect(os.environ.get("DATABASE_URI"))

db_uri = os.environ.get("DATABASE_URI")
print(db_uri)
connection = psycopg2.connect(db_uri)

def get_polls():
    with connection: 
        with connection.cursor() as cursor: 
            cursor.execute(SELECT_POLLS)
            return cursor.fetchall()

def get_options(poll_id: int):
    with connection: 
        with connection.cursor() as cursor: 
            cursor.execure(SELECT_OPTIONS_IN_POLL, (poll_id,))
            return cursor.fetchall()
