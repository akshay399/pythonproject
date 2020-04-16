import sqlite3


def theaterCreator():

	conn=sqlite3.connect('theater.db')
	c=conn.cursor()

	c.execute("""CREATE TABLE IF NOT EXISTS seat (
				type text,
				price integer,
				seatnum varchar
				movie_name varchar references movie(name)
				
			)""")
	conn.commit()

	c.execute("""CREATE TABLE IF NOT EXISTS movie (
				name varchar,
				timing varchar,
				poster varchar
				
			)""")
	c.execute("""CREATE TABLE IF NOT EXISTS receipt (
				receiptNum varchar,
				seats varchar,
				price integer,
				movie varchar
				
			)""")

	conn.commit()
	conn.close()
if __name__ == '__main__':

	conn=sqlite3.connect('theater.db')
	c=conn.cursor()
	c.execute('''SELECT * FROM receipt''')
	print(c.fetchall())
	