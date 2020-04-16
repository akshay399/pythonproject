# import sys
# sys.path.append('/home/litshit/practice/projects/Pyhton/booking_management_system/source')

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "source"))
from tkinter import *
#from functools import partial
from login import *
from regnew import *
from tkinter import *
from theaterdbcreator import *
from userdbcreator import *
from functools import partial
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect('user.db')
c=conn.cursor()

def main_screen():
    userCreator()
    theaterCreator()
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text="",width="300",height="2",font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login",height="2",width="30",command=lambda:login_screen(screen)).pack()
    Label(text="").pack()
    Button(text="Register",height="2",width="30",command=lambda:reg_screen(screen)).pack()
    screen.mainloop()
    #root.mainloop()
    #tkWindow.mainloop()

main_screen()
