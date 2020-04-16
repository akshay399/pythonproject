from tkinter import *
from functools import partial
from tkinter import messagebox
import sqlite3
from tkinter import *
#from functools import partial
from abcdef import *

conn=sqlite3.connect('user.db')
c=conn.cursor()

def reg_user():
    username_info=username.get()
    email_info=email.get()
    password_info=password.get()

    # print(username_info)
    # print(password_info)

    c.execute('''SELECT name FROM user''')
    a=c.fetchall()
    
    
    constr1,constr2="@",".com"
    
    if((email_info.find(constr1))>0 and (email_info.find(constr2))>0):
        
        try :
            
            c.execute('''INSERT INTO user(passwd,name,mail) VALUES (?,?,?) ''',(password.get(),username.get(),email.get()))
            Label(screen1,text="Registered sucessfully",fg="green",font=("calibri",11)).pack()

            text=str("Dear"+username_info+","+"\nThank you for registering on QUICK BOOK. Your registration has been received, thanks!\nThese are your details:"+"\nUsername:"+username_info+"\nPassword:"+password_info+"\nPlease don't share them with anyone")
            subject="REGISTRATION SUCCESSFUL"
            mailSender(email_info,text,subject)
            c.execute("SELECT * FROM user")
            a=c.fetchall()
            print(a)
            conn.commit()



    
        
        except sqlite3.IntegrityError:
            messagebox.showinfo('ERROR','Username already taken !')
            username_entry.delete(0,END)



        
        
    else:
        #execute a dialogue box
        messagebox.showinfo('ERROR','Enter valid mail-id')


    username_entry.delete(0,END)
    password_entry.delete(0,END)
    email_entry.delete(0,END)

    
    

def reg_screen(screen):
	
    global screen1
    screen1=Toplevel(screen)
    screen1.title("REGISTRATION PAGE")
    screen1.geometry("300x300")

    global username
    global email
    global password
    global username_entry
    global email_entry
    global password_entry
    username=StringVar()
    password=StringVar()
    email=StringVar()

    Label(screen1,text="ENTER DETAILS BELOW",bg="grey",width="300",height="2",font=("Calibri",13)).pack()
    Label(text="").pack()

    # Label(screen1,text="Please enter details below").pack()
    # Label(screen1,text="").pack()

    Label(screen1,text="",width="30",height="1",font=("Calibri",13)).pack()
    Label(text="").pack()
    
    Label(screen1,text="Username:").pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    #Entry(screen1,textvariable=username).pack()

    Label(screen1,text="Email:").pack()
    email_entry=Entry(screen1,textvariable=email)
    email_entry.pack()
    
    Label(screen1,text="Password:").pack()
    #password_entry=Entry(screen1,textvariable=password)
    password_entry=Entry(screen1,textvariable=password,show='*')
    password_entry.pack()
    Label(screen1,text="").pack()
    
    Button(screen1,text="REGISTER",width=10,height=1,command=reg_user).pack()