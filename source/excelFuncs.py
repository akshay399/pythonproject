import openpyxl
from openpyxl.utils import *
from openpyxl import Workbook
from tkinter import messagebox
from seatselection import *
import tkinter as tk


def isHousefull(sheet):
	count=0
	
	for ro in range(1,11):
		for colum in range(1,6):
			if((sheet.cell(row=ro,column=colum).value) is not None ):
				count=count+1

	if count==50:
		return True
	
	else:
		return False
	

def fillCell(sheet,Button_number,username):
	
	sheet[Button_number]=username


	

def isCellFull(sheet,cell_number):
	if sheet[cell_number].value:
		return True
	else:
		return False
	


def getFilledCells(sheet):
	
	letter=['A','B','C','D','E']
	
	filled_Cells=[]
	
	for row in letter:
		for col in range(1,11):
			item=str(row+str(col))
			if isCellFull(sheet,item):
				filled_Cells.append(item)

	return filled_Cells


	


	# root=tk.Tk()

	
	# onClickMovie(root,'Kalank')

	# root.mainloop()
                            
                            




