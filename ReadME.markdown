# MOVIE TICKET BOOKING SYSTEM

Our project basically manages the ticket booking process of a theater,
providing an interface to the user to book movie tickets in a more easy
way. The project proceeds through a sequence of well-designed forms
provided with validations to ensure consistency, reliability and most
importantly correctness of information fed into the database

## SOLUTION DESIGN

We used tkinter toolkit for GUI. we Incorporated some widgets which
better the result screen , so that the user can use the application with
no confusion. The overall architecture can be thought of having two main parts :

-   The user side

-   The admin side

### The user side :

This portion of the application is exclusively for the user who uses the
app for booking the tickets.This portion consists of the following
windows

#### 1.  Home Screen

 This is the page the user will see when he opens the application or
 (runs main.py).

 ![](.//media/image2.png)

If he is using the application for the first time he can click on
Register and register himself. Else he can Login using his Credentials
and move forward

#### 2.  Register Screen

 This page is for users who are using the app for the first time . Here
 users can register using his/her email id and password . Then an email
 will be sent to his email id , which confirms his/her registration.

 ![](.//media/image1.png)

#### 3.  Login Screen

 Users who have already registered before can straightaway login using
 their username,password and start booking.

 ![](.//media/image3.png)

#### 4.  Now Showing Screen

 This screen is shown after the login/registration process . It shows a
 list of the movies currently being shown at the theatre. The user has
 to select one among and click confirm.On clicking confirm a poster of
 that movie will pop up . On clicking on that poster you will be taken
 to the seat selection Screen where you can select the seats you want
 to book.

 ![](.//media/image7.png)![](.//media/image6.png)

#### 4.  Seat Selection Screen

 On this screen there is a grid of seats just like the one in a theater
 . User will have to select the seats of his choice from the available
 seats . On clicking confirm the seats will be booked and the session
 code or receipt code will be sent to you via mail.

![](.//media/image5.png)

As you can see in the above image , the seats which have been booked
already are displayed differently as labels and the available seats are
displayed as buttons which can be clicked.

### The admin side :

This portion is for the admin or the owner of the theatre or the booking
counter at the theatre . Now the receipt code which the user has been
allotted will be entered in the window and the booking will be confirmed
and he will be allowed entry in the theater.

![](.//media/image4.png)

## IMPLEMENTATION PLAN

We have used PYTHON language and specifically Tkinter toolkit for the
GUI package. We have used sqlite3 for the database management of the
users . And we have used MS Excel ( via openpyxl module ) to maintain a
record of booked seats .


## HOW TO RUN LOCALLY 

1. Go to the Project folder in your system

2. First do the entire setup
 - `pip install tkinter`,
 - `pip install openpyxl`,
 - `pip install smtplib`,
 
3. Run `main.py`

4. After completing the booking process close all the windows and run `adminside.py`.


## Contributors

- Nishit Jain 
> - [LinkedIn](www.linkedin.com/in/nishit-jain1)
> - [GitHub](https://github.com/coldkillerr)
- Akshay Chopade
> - [LinkedIn](https://www.linkedin.com/in/akshay-chopade-19307a172)
> - [GitHub](https://github.com/akshay399)

- Deep Patil




   













