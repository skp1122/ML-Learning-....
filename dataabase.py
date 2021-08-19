import sqlite3
#conn=sqlite3.connect(':memory:')
conn=sqlite3.connect('customer.db')
c=conn.cursor()
c.exute("""CREATE TABLE customers(
		first_name text,
		last_name text,
		email text
		)""")
#NULL INTEGER REAL TEXT BLOB-data types in sqlite
#commit command
conn.commit()
#close connection
conn.close()
