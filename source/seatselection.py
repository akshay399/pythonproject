#try using append instead of row[column]=

from tkinter import *
from onClickFuncs import *
import openpyxl
from openpyxl.utils import *
from openpyxl import Workbook
from tkinter import messagebox
from seatselection import *
import tkinter 
from excelFuncs import *
import random
import string
from theaterdbcreator import *
from abcdef import *

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


button_identities = []
# functions for gui

def onClickSeatButton(Button,username,sheet):
    # print('button index=',i)
    # print('button identity=',button_identities[i])
    # Button=(button_identities[i])
    # print('button=',Button)
    Button_number=Button.cget('text')
    # messagebox.showinfo('',Button_number)

    fillCell(sheet,Button_number,username)
    try:
        Button.configure(state=tk.DISABLED)
    except:
        Button.configure(state="disabled")

    
            

    # Label(screen,text=Button_number+' Selected',fg="green",font=("calibri",11)).pack()


def getSelected(rows):
    selected=[]
    for button in rows:
        if (button['state'] =="disabled"):
            print(button,'selected')
            seatNum=button.cget('text')
            selected.append(seatNum)

    return selected



def onClickConfirmButton(mainwindow,allSeats,email,username,movie_name):

   

    selectedSeats=getSelected(allSeats)
    
    if not selectedSeats:
        messagebox.showinfo('Warning','You Selected nothing !!')
    else:
        messagebox.showinfo('Message','You Selected :\n'+str(selectedSeats))
        i=1
        # seatlist=[]
        gold=[]
        silver=[]
        bronze=[]

        for seat in selectedSeats:
            if (seat[0] in ['A','B']):
                print('seat[0]:',seat[0])
                print('gold:',seat)
                gold.append(seat)
            elif(seat[0] in ['C','D']):
                print('seat[0]:',seat[0])
                print('silver :',seat)
                silver.append(seat)
            else:
                print('seat[0]:',seat[0])
                print('bronze :',seat)
                bronze.append(seat)

        price=len(gold)*250 +len(silver)*200 +len(bronze)*150
        receiptNum=randomString(10)
        seatStr=','.join(selectedSeats)
        print('Seat String : ',seatStr)
        
        theaterCreator()
        conn=sqlite3.connect('theater.db')
        c=conn.cursor()
        c.execute('''INSERT INTO receipt(receiptNum,seats,price,movie) VALUES (?,?,?,?) ''',(receiptNum,seatStr,price,movie_name))
        conn.commit()
        conn.close()

        text='Dear '+username+',\n'+'Your one time receipt-code : \n'+receiptNum+'\nPlease do not share it with anyone'
        mailSender(email,text,'BOOKING SUCCESSFULL')




# the GUI

def seatSelection(mainwindow,sheet,email,username,movie_name):
    
    # btn=[]
    filled=getFilledCells(sheet)
    # print(filled)

    # root=Tk()
    # mainwindow=root
    button_identities=[]

    # # screen this side
    # label=Label(root,text="Screen this side",padx=5,pady=5,font=("Arial",18))
    # label.pack()

    # # horizontal blue line
    # verticalFrame=Frame(root,bg="blue")
    # verticalFrame.grid()

    # label=Label(root,text="",fg="white",padx=5,pady=5)
    # label.grid()

    mainframe=Frame(mainwindow)
    mainframe.pack(fill="both",expand=True)

    # label=Label(mainframe,text="",fg="white",padx=5,pady=5)
    # label.config(font=("Arial",18))
    # label.pack(fill="x")

    label=Label(mainframe,bg='black',fg='white',text="Screen this side",padx=5,pady=5)
    label.config(font=("Arial",18))
    label.pack(fill="x")
    #vertical layout with data
    verticalFrame=Frame(mainframe,bg="blue")

    #item1=Label(verticalFrame,text="Item 1",bg="orange",padx=10,pady=10,fg="white")
    #item1.pack(fill="x",padx=10,pady=10)

    #item1=Label(verticalFrame,text="Item 2",bg="yellow",padx=10,pady=10,fg="black")
    #item1.pack(fill="x",padx=10,pady=10)

    #item1=Label(verticalFrame,text="Item 3",bg="green",padx=10,pady=10,fg="white")
    #item1.pack(fill="x",padx=10,pady=10)

    verticalFrame.pack(fill="x")
    #end vertical

    #horizontal
    #label=Label(mainframe,text="Horizontal Frame Example",bg="black",fg="white",padx=5,pady=5)
    label.config(font=("Arial",18))
    label.pack(fill="x")
    horizontal_frame=Frame(mainframe)

    #label1.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
    #label1=Label(horizontal_frame,text="Item 1 in Horizontal",bg="red",fg="white",padx=10,pady=10)
    #label1=Label(horizontal_frame,text="Item 2 in Horizontal",bg="red",fg="white",padx=10,pady=10)
    #label1.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")
    #label1=Label(horizontal_frame,text="Item 3 in Horizontal",bg="red",fg="white",padx=10,pady=10)
    #label1.grid(row=0,column=2,padx=10,pady=10,sticky="nsew")
    #label1=Label(horizontal_frame,text="Item 4 in Horizontal",bg="red",fg="white",padx=10,pady=10)
    #label1.grid(row=0,column=3,padx=10,pady=10,sticky="nsew")

    horizontal_frame.grid_columnconfigure(0,weight=1)
    horizontal_frame.grid_columnconfigure(1,weight=1)
    horizontal_frame.grid_columnconfigure(2,weight=1)
    horizontal_frame.grid_columnconfigure(3,weight=1)
    horizontal_frame.pack(fill="x")

    #end horizontal

    #grid data

    label=Label(mainframe,text="",fg="white",padx=5,pady=5)
    label.config(font=("Arial",18))
    label.pack(fill="x")

    grid_frame=Frame(mainframe)



    item=[]
    letters=['A','B','C','D','E']

    for i in range(50):
        
        if(i+1<11):
            item.append(str(letters[0]+str(i+1)))

        elif(i+1<21):
            item.append(str(letters[1]+str(i-9)))

        elif(i+1<31):
            item.append(str(letters[2]+str(i-19)))

        elif(i+1<41):
            item.append(str(letters[3]+str(i-29)))

        elif(i+1<51):
            item.append(str(letters[4]+str(i-39)))


    i=0
    
    if item[i] not in filled:
        btnA1=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA1,username,sheet))
        btnA1.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)
        button_identities.append(btnA1)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)
    i+=1

    if item[i]  not in filled:
        btnA2=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA2,username,sheet))
        btnA2.grid(row=0,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)
        button_identities.append(btnA2)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)
    
    i+=1

        

        
    if item[i]  not in filled:
        btnA3=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA3,username,sheet))
        btnA3.grid(row=0,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)
        button_identities.append(btnA3)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)

    i+=1


    if item[i] not  in filled:

        btnA4=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA4,username,sheet))
        btnA4.grid(row=0,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)
        button_identities.append(btnA4)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)


    i+=1

    if item[i] not  in filled:
        btnA5=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA5,username,sheet))
        btnA5.grid(row=0,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)
        button_identities.append(btnA5)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)

    i+=1


    if item[i] not  in filled:

        btnA6=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA6,username,sheet))
        btnA6.grid(row=0,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)
        button_identities.append(btnA6)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)

    i+=1
    
    if item[i] not  in filled:

        btnA7=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA7,username,sheet))
        btnA7.grid(row=0,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
        button_identities.append(btnA7)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
    
    i+=1


    if item[i] not  in filled:
        btnA8=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA8,username,sheet))
        btnA8.grid(row=0,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)
        button_identities.append(btnA8)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)

    i+=1
    if item[i] not  in filled:
        btnA9=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA9,username,sheet))
        btnA9.grid(row=0,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)
        button_identities.append(btnA9)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)

    i+=1


    if item[i] not  in filled:
        btnA10=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnA10,username,sheet))
        btnA10.grid(row=0,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)
        button_identities.append(btnA10)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=0,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)

    i+=1

    if item[i] not  in filled:
        btnB1=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB1,username,sheet))
        btnB1.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)
        button_identities.append(btnB1)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)


    i+=1

    if item[i] not  in filled:

        btnB2=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB2,username,sheet))
        btnB2.grid(row=1,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)
        button_identities.append(btnB2)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)

    i+=1

    if item[i] not  in filled:

        btnB3=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB3,username,sheet))
        btnB3.grid(row=1,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)
        button_identities.append(btnB3)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)

    i+=1
    

    if item[i] not  in filled:

        btnB4=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB4,username,sheet))
        btnB4.grid(row=1,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)
        button_identities.append(btnB4)
    
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)


    i+=1


    if item[i] not  in filled:

        btnB5=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB5,username,sheet))
        btnB5.grid(row=1,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)
        button_identities.append(btnB5)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)

    i+=1
    
    if item[i] not  in filled:

        btnB6=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB6,username,sheet))
        btnB6.grid(row=1,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)
        button_identities.append(btnB6)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)


    i+=1
    if item[i] not  in filled:

        btnB7=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB7,username,sheet))
        btnB7.grid(row=1,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
        button_identities.append(btnB7)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
    

    i+=1
    if item[i] not  in filled:
        btnB8=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB8,username,sheet))
        btnB8.grid(row=1,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)
        button_identities.append(btnB8)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)
    i+=1
    
    if item[i] not  in filled:
        btnB9=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB9,username,sheet))
        btnB9.grid(row=1,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)
        button_identities.append(btnB9)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)
    i+=1
    if item[i] not  in filled:
        btnB10=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnB10,username,sheet))
        btnB10.grid(row=1,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)
        button_identities.append(btnB10)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=1,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)
    i+=1
    if item[i] not  in filled:
        btnC1=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC1,username,sheet))
        btnC1.grid(row=2,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)
        button_identities.append(btnC1)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)
    i+=1
    if item[i] not  in filled:
        btnC2=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC2,username,sheet))
        btnC2.grid(row=2,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)
        button_identities.append(btnC2)

    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)
    i+=1
    if item[i] not  in filled:
        btnC3=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC3,username,sheet))
        btnC3.grid(row=2,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)
        button_identities.append(btnC3)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)
    i+=1
    if item[i] not  in filled:
        btnC4=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC4,username,sheet))
        btnC4.grid(row=2,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)
        button_identities.append(btnC4)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)
    i+=1
    if item[i] not  in filled:
        btnC5=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC5,username,sheet))
        btnC5.grid(row=2,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)
        button_identities.append(btnC5)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)
    i+=1
    if item[i] not  in filled:
        btnC6=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC6,username,sheet))
        btnC6.grid(row=2,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)
        button_identities.append(btnC6)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)
    i+=1
    if item[i] not  in filled:
        btnC7=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC7,username,sheet))
        btnC7.grid(row=2,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
        button_identities.append(btnC7)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
    i+=1
    if item[i] not  in filled:
        btnC8=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC8,username,sheet))
        btnC8.grid(row=2,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)
        button_identities.append(btnC8)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)

    i+=1
    if item[i] not  in filled:
        btnC9=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC9,username,sheet))
        btnC9.grid(row=2,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)
        button_identities.append(btnC9)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)
    i+=1
    if item[i] not  in filled:
        btnC10=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnC10,username,sheet))
        btnC10.grid(row=2,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)
        button_identities.append(btnC10)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=2,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)
    i+=1
    if item[i] not  in filled:
        btnD1=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD1,username,sheet))
        btnD1.grid(row=3,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)
        button_identities.append(btnD1)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)
    i+=1
    if item[i] not  in filled:
        btnD2=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD2,username,sheet))
        btnD2.grid(row=3,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)
        button_identities.append(btnD2)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)
    i+=1
    if item[i] not  in filled:
        btnD3=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD3,username,sheet))
        btnD3.grid(row=3,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)
        button_identities.append(btnD3)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)
    i+=1
    if item[i]  not in filled:
        btnD4=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD4,username,sheet))
        btnD4.grid(row=3,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)
        button_identities.append(btnD4)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)
    i+=1
    if item[i] not  in filled:
        btnD5=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD5,username,sheet))
        btnD5.grid(row=3,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)
        button_identities.append(btnD5)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)
    i+=1
    if item[i] not  in filled:
        btnD6=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD6,username,sheet))
        btnD6.grid(row=3,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)
        button_identities.append(btnD6)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)
    i+=1
    if item[i] not  in filled:
        btnD7=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD7,username,sheet))
        btnD7.grid(row=3,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
        button_identities.append(btnD7)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
    i+=1
    if item[i] not  in filled:
        btnD8=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD8,username,sheet))
        btnD8.grid(row=3,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)
        button_identities.append(btnD8)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)
    i+=1
    if item[i] not  in filled:
        btnD9=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD9,username,sheet))
        btnD9.grid(row=3,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)
        button_identities.append(btnD9)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)
    i+=1
    if item[i] not  in filled:
        btnD10=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnD10,username,sheet))
        btnD10.grid(row=3,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)
        button_identities.append(btnD10)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=3,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)
    i+=1
    if item[i] not  in filled:
        btnE1=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE1,username,sheet))
        btnE1.grid(row=4,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)
        button_identities.append(btnE1)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=0,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(0,weight=1)
    i+=1
    if item[i] not  in filled:
        btnE2=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE2,username,sheet))
        btnE2.grid(row=4,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)
        button_identities.append(btnE2)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=1,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(1,weight=1)
    i+=1    
    if item[i] not  in filled:
        btnE3=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE3,username,sheet))
        btnE3.grid(row=4,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)
        button_identities.append(btnE3)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=2,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(2,weight=1)
    i+=1
    if item[i] not  in filled:
        btnE4=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE4,username,sheet))
        btnE4.grid(row=4,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)
        button_identities.append(btnE4)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=3,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(3,weight=1)
    i+=1
    if item[i] not  in filled:
        btnE5=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE5,username,sheet))
        btnE5.grid(row=4,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)
        button_identities.append(btnE5)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=4,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(4,weight=1)
    i+=1
    if item[i] not  in filled:
        btnE6=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE6,username,sheet))
        btnE6.grid(row=4,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)
        button_identities.append(btnE6)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=5,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(5,weight=1)
    i+=1
    if item[i] not  in filled:
        btnE7=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE7,username,sheet))
        btnE7.grid(row=4,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
        button_identities.append(btnE7)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=6,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(6,weight=1)
    i+=1
    if item[i] not  in filled:
        btnE8=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE8,username,sheet))
        btnE8.grid(row=4,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)
        button_identities.append(btnE8)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=7,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(7,weight=1)
    i+=1
    if item[i] not  in filled:
        btnE9=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE9,username,sheet))
        btnE9.grid(row=4,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)
        button_identities.append(btnE9)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=8,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(8,weight=1)
    i+=1
    if item[i]  not in filled:
        btnE10=Button(grid_frame,text=item[i],bg="gold",fg="black",command=lambda:onClickSeatButton(btnE10,username,sheet))
        btnE10.grid(row=4,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)
        button_identities.append(btnE10)
    else:
        lbl=Label(grid_frame,text=item[i],bg="gold",fg="black").grid(row=4,column=9,padx=5,pady=5,sticky="nsew")
        grid_frame.grid_columnconfigure(9,weight=1)

    


    Label(mainwindow,text="",width="100",height="2",font=("Calibri",13)).pack()
    Label(mainwindow,text="").pack()
    Button(mainwindow,text="CONFIRM",width='30',height='2',command=lambda:onClickConfirmButton(mainwindow, button_identities,email,username,movie_name)).pack()
    Label(mainwindow,text="",width="100",height="2",font=("Calibri",13)).pack()
    Label(mainwindow, text="").pack()

    # for button in button_identities:
    #     print(button)


    grid_frame.pack(fill="x")


    





# mainW=Tk()
# seatSelection(mainW)
# mainW.mainloop()

