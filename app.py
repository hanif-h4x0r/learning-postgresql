import psycopg2

conn = psycopg2.connect(
		dbname="mydb",
		user="h4x0r",
		password="h4x0r",
		host="localhost",
		port="5432"	
		)
print("Connected to PostgreSQL!")

conn.close()
