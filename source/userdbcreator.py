import sqlite3


def userCreator():
	conn=sqlite3.connect('user.db')

	c=conn.cursor()

	c.execute("""CREATE TABLE IF NOT EXISTS user (
				passwd text,
				name text PRIMARY KEY,
				mail text, 
				receipt_code varchar 


			)""")
	conn.commit()
	conn.commit()
	# print(c.fetchall())
	conn.close()






# c.execute("""CREATE TABLE IF NOT EXISTS ticket (
# 			rec_num varchar,
# 			mail_id varchar references user(mail),
# 			seatnum integer references seat(seatnum),
# 			price integer references seat(price),
			
			

# 		)""")
# conn.commit()



#c.execute("SELECT * FROM user")


# c.execute('''SELECT * from user''' )
# print(c.fetchall())
