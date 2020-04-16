import openpyxl
from openpyxl.utils import *
from openpyxl import Workbook
from tkinter import messagebox
from seatselection import *
import tkinter as tk
from excelFuncs import *
import random
import string
from theaterdbcreator import *
from abcdef import *



def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



def onClickMovieBook(prescreen,movie_name,email,username):
	prescreen.quit()
	wb=openpyxl.load_workbook('movies.xlsx')
	
	try:
		sheet=wb.get_sheet_by_name(movie_name)
	except KeyError:
		print('Key error Excepted')
		wb.create_sheet(movie_name)
		sheet=wb.get_sheet_by_name(movie_name) 

	wb.save('movies.xlsx')
	# print(isHousefull(sheet))
	if isHousefull(sheet):

		messagebox.showinfo('OOPS !!','SHOW IS FULL !')
	else:

		# messagebox.showinfo('','BOOK YOUR SEATS HERE')
		# seat selector GUI goes here
		# filled_Cells=getFilledCells(sheet)
		screen=tk.Tk()
		seatSelection(screen,sheet,email,username,movie_name)
		screen.mainloop()

	wb.save('movies.xlsx')





def onClickConfirmButton(selectedSeats,email):
	i=1
	seatlist=[]
	gold=[]
	silver=[]
	bronze=[]

	for seat in selectedSeats:
		if (seat[0]==x for x in ['A','B']):
			gold.append(seat)
		if(seat[0]==x for x in ['C','D']):
			silver.append(seat)
		else:
			bronze.append(seat)

	price=len(gold)*150 +len(silver)*200 +len(bronze)*250
	receiptNum=randomString(10)
	seatStr=','.join(seatlist)
	
	theaterCreator()
	conn=sqlite3.connect('theater.db')
	c=conn.cursor()
	c.execute('''INSERT INTO receipt(receiptNum,seats,price) VALUES (?,?,?) ''',(receiptNum,seatStr,price))

	text='Your one time receipt-code : \n'+receiptNum+'\nPlease do not share it with anyone'
	mailSender(email,text,'BOOKING SUCCESSFULL')



 