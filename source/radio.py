
# Importing Tkinter module 
from tkinter import * 
from tkinter.ttk import *
from movieimagge import *
import tkinter
 
def onClickLogin(username,email) :
	# Creating master Tkinter window 
	
	master=Tk()



	  
	# Tkinter string variable 
	# able to store any string value 
	v = StringVar(master, "1") 
	  
	# Style class to add style to Radiobutton 
	# it can be used to style any ttk widget 
	style = Style(master) 
	style.configure("TRadiobutton", background = "white",  
	                foreground = "black", font = ("arial", 10, "bold")) 
	  
	# Dictionary to create multiple buttons 
	values = {"Avatar" : "Avatar", 
	          "Avengers" : "Avengers", 
	          "Spiderman" : "Spiderman",
	          "Wolf Of Wall Street" : "Wolf_Of_Wall_Street"} 
	  
	# Loop is used to create multiple Radiobuttons 
	# rather than creating each button separately 
	for (text, value) in values.items(): 
		lbl=Label().pack()
		Radiobutton(master, text = text, variable = v,value = value).pack(side = TOP, ipady = 5) 


	lbl=Label().pack()
	CnfrmBtn=Button(master,text="CONFIRM",command=lambda:moviePage( username , email , str(v.get()))).pack(side = TOP, ipady = 5)
	master.mainloop()
	


