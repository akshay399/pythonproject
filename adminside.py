import sys
sys.path.append('/home/litshit/booking_management_system/source')
from tkinter import *
#from functools import partial
from tkinter import *
from functools import partial
from tkinter import messagebox
import sqlite3
from tkinter import *
#from functools import partial
from theaterdbcreator import *
from abcdef import *


def getDetails(rec_code,screen):
    code=rec_code.get()
    print(code)
    # screen.destroy()
    theaterCreator()
    
    conn=sqlite3.connect('theater.db')
    c=conn.cursor()
    
    c.execute('''SELECT price FROM receipt WHERE receiptNum = (?)''',(code,))
    price=c.fetchall()

    c.execute('''SELECT seats FROM receipt WHERE receiptNum = (?)''',(code,))
    seats=c.fetchall()

    c.execute('''SELECT movie FROM receipt WHERE receiptNum = (?)''',(code,))
    movie=c.fetchall()

    screenA=Tk()
    displayReceipt(screenA,code,price,seats,movie)
    screenA.mainloop()


def displayReceipt(screen,code,price,seats,movie):
    root=screen
    print('price : ',price)
    print('seats : ',seats)
    print('movie :',movie)
    
    for tup in price:
        pri=tup[0]

    for tupl in seats:
        sea=tupl

    for tuplee in movie:
        mov=tuplee

    
    Label(root,text='Receipt Code : '+ str(code) ,width="30",height="1",font=("Calibri",13)).pack(fill="x")
    Label(text="").pack()

    Label(root,text='seats : '+ str(sea) ,width="30",height="1",font=("Calibri",13)).pack(fill="x")
    Label(text="").pack()

    Label(root,text='Price : '+ str(pri) ,width="30",height="1",font=("Calibri",13)).pack(fill="x")
    Label(text="").pack()

    Label(root,text='Movie : '+ str(mov) ,width="30",height="1",font=("Calibri",13)).pack(fill="x")
    Label(text="").pack()

    


def adminSide(screen2):

    # global screen2
    # screen2=Toplevel(screen)
    screen2.title("LOGIN PAGE")
    screen2.geometry("300x250")

    global receipt_code
    receipt_code=StringVar()

    Label(screen2,text="",width="30",height="1",font=("Calibri",13)).pack()
    Label(text="").pack()

    Label(screen2,text="Enter receipt code").pack()
    Entry(screen2,textvariable=receipt_code).pack()

    Label(screen2,text="",width=30,height=1,font=("Calibri",13)).pack()

    Button(screen2,text="LOGIN",width=10,height=1,command=lambda:getDetails(receipt_code,screen2)).pack()
    

def main():
    mainScreen=Tk()
    adminSide(mainScreen)
    mainScreen.mainloop()

if __name__ == '__main__':
    main()

