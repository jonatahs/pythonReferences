import psycopg2

# connecting to postgre database with credentials
conn= psycopg2.connect(
    host="localhost",
    database="database",
    user="user",
    password="123")

cur = conn.cursor()
