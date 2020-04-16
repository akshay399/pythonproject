import tkinter
from distutils import command
from tkinter import *
from tkinter import messagebox
from onClickFuncs import *
from tkinter import *
#from functools import partial
from tkinter import *
from functools import partial
from tkinter import messagebox
import sqlite3
from tkinter import *
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "source"))






def btnclick(screen,username,email,movie_name):
	onClickMovieBook(screen,movie_name,email,username)
	
    # messagebox.showinfo("Message", "Button is clicked")



# def buttonFun():
#     print("Choose your seat!")


def moviePage(username,email,movie_name):
	print('moviePage started......')
	root = Toplevel()
	root.geometry("800x800")
	# movie_name='Avatar'

	photo = PhotoImage(file='source/images/'+movie_name +'.png')
	# photo2 = PhotoImage(file="m3.png")
	btn = Button(
	    root,
	    image=photo,
	    command=lambda:btnclick(root,username,email,movie_name),
	    border=0
	)
	btn.pack(pady=50,padx=50)

	# b = Button(root, text="BOOK")
	# b.pack()

	# b2 = Button(root, text="NEXT MOVIE")
	# b2.pack(pady=29)


	root.mainloop()

# btn2 = Button(
#   root,
#  image=photo2,
# command=btnclick,
# border=0,
# )
# btn2.pack()

