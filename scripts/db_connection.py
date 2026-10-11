import os
import psycopg2

connection = psycopg2.connect(
    host="127.0.0.1",
    database="walmart_db",
    user="postgres",
    password=os.environ["DB_PASSWORD"]
)

print("Connected to PostgreSQL successfully!")

connection.close()