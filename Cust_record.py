from tkinter import *                                                                       #import the header to make GUI
import mysql.connector                                              # importing to make a connection with the SQL.
from mysql.connector import MySQLConnection,Error                       # importing specific Library.
try:                                                                                                                    #Exception Handeling
    print("Connecting....")
    conn=mysql.connector.connect(host='localhost',user='root',password='root',database='prachi')             #Establish a Connection with the database
    if conn.is_connected(): #Checking for the connection.
        print("Connection Established:")
        c=conn.cursor()             # Creating a handler to fire the Querry.
        c.execute("DROP TABLE IF EXISTS CUSTOMER")  #Executing a SQL querry
        c.execute("CREATE TABLE CUSTOMER(cust_id char(4),custname char(20),age char(4),address char(20))")
        print("Table created.")
        p=Tk() #Creating Tikinter window (GUI).
        p.title("Bank_work") #Giving title
        def insert():   #A new Function (Insert data in data base). 
            h=w.get()  #Declaring var to store the values from GUI.  
            j=x.get()
            k=y.get()
            l=z.get()
            q1="INSERT INTO CUSTOMER VALUES('{}','{}',{},'{}')".format(h,j,k,l)  #To use User inputes in the Querry.
            c.execute(q1)
            print("Row inserted")
            
        def delete():   #A new Function (Delete data from database). 
            h=w.get()       #Declaring var to store the values from GUI. 
            q2="DELETE FROM CUSTOMER WHERE cust_id='{}'".format(h)       #To use User inputes in the Querry.
            c.execute(q2)
            print("Row deleted")
            
        def update():            #A new Function (Update data from the database). 
            h=w.get()                 #Declaring var to store the values from GUI. 
            j=x.get()
            q3="UPDATE CUSTOMER SET custname='{}' WHERE cust_id='{}'".format(j,h)        #To use User inputes in the Querry.
            c.execute(q3)
            print("Record modified")

        def see():             #A new Function (Look at all the data stored in the database). 
            q4="SELECT * FROM CUSTOMER"
            c.execute(q4)
            result=c.fetchall()     #Helps to store all the records from Database (Stored in the List format).
            print("CUST_ID\tCUSTNAME\tAGE\tADDRESS")
            for row in result:          #To traverse from the data.
                cid=row[0]
                cname=row[1]
                age=row[2]
                addr=row[3]
                print(cid,'\t',cname,'\t\t',age,'\t',addr)
        def close():
            p.destroy()

        w=StringVar()       #GUI data is stored here
        x=StringVar()
        y=StringVar()
        z=StringVar()
        Label(p,text='Choose any one').grid(row=0,column=0)     #Creating a Label
        Button(p,text='close',command=close).grid(row=0,column=1)       #Creating a Button
        Button(p,text='SEE-DB',command=see).grid(row=0,column=2)
        Label(p,text='Cust_id').grid(row=1,column=0)
        Entry(p,textvariable=w).grid(row=1,column=1)         #Creating a TextField
        Label(p,text='Custname').grid(row=2,column=0)
        Entry(p,textvariable=x).grid(row=2,column=1)
        Label(p,text='Age').grid(row=3,column=0)
        Entry(p,textvariable=y).grid(row=3,column=1)
        Label(p,text='Address').grid(row=4,column=0)
        Entry(p,textvariable=z).grid(row=4,column=1)
        Button(p,text='add',command=insert).grid(row=5,column=0)
        Button(p,text='delete',command=delete).grid(row=5,column=1)
        Button(p,text='update',command=update).grid(row=5,column=2)
        p.mainloop()            #All the fields is set on the GUI Window
except Error as e:              #If any unknown error Occured.
    print(e)
finally:                                    #The block that always gets executed.
    conn.commit()               #Saving all the data to database.
    conn.close()                    #closing the connection with the SQL.
    print("End of program")
