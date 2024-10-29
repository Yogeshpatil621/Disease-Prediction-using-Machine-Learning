import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox as tkMessageBox

def database():
    global conn, cursor
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    q1 = "Create table if not exists user (id integer primary key AUTOINCREMENT,email varchar(150) unique,password TEXT, name TEXT,phone_no TEXT)"
    cursor.execute(q1)


def login():
    root = Tk()
    em=StringVar(root)
    passwrd=StringVar(root)
    root.title("disease prediction system")
    root.geometry("780x450")
    root.config(bg='gray10')
    def log_in():
        database()
        e = em.get()
        p = passwrd.get()
        cursor.execute(f'SELECT * FROM user WHERE email = ? AND password = ?', (e, p))
        data=cursor.fetchone()

        if data:
            tkMessageBox.showinfo("disease prediction system","Logged In Successfully !!!")
            root.destroy()
            import disease_prediction
        else:
            tkMessageBox.showinfo("disease prediction system","Failed To Login !!!")
            em.set("")
            passwrd.set("")
            
    h1 = Label(root, text="-- LOGIN --",font=("",24,"bold"),bg='gray10',fg="white")
    h1.place(x=300,y=15)
    h2 = Label(root, text="Email: ",font=("",20,"bold"),bg='gray10',fg="white")
    h2.place(x=114,y=120)
    h3 = Label(root, text="Password: ",font=("",20,"bold"),bg='gray10',fg="white")
    h3.place(x=60,y=205)
    e1 = Entry(root,textvariable=em,font=("",20),width=30)
    e1.place(x=250,y=120)
    e2 = Entry(root,textvariable=passwrd,font=("",20),width=30,show='*')
    e2.place(x=250,y=205)
    b1 = Button(root, text="Register",font=("",20,"bold"),bd=2,relief="solid",width=18,command=signup)
    b1.place(x=60,y=290)
    b2 = Button(root, text="LOGIN",font=("",20,"bold"),bd=2,relief="solid",width=18,command=log_in)
    b2.place(x=390,y=290)
    root.mainloop()

def signup():
    global nme,passwrd,em,phone,branch,year
    root2 = Tk()
    root2.config(bg='gray10')
    nme=StringVar(root2)
    passwrd=StringVar(root2)
    em = StringVar(root2)
    phone = StringVar(root2)

    root2.title("disease prediction system")
    root2.geometry("780x500")
    def reg():
   
        global nme,passwrd,em,phone
        database()
        cursor.execute(f"INSERT INTO user(name,password,email,phone_no) VALUES('{nme.get()}','{passwrd.get()}','{em.get()}','{phone.get()}')")
        conn.commit()
        conn.close()
        tkMessageBox.showinfo("disease prediction system","Registered Successfully !!!")
        root2.destroy()
        login()
        
    h1 = Label(root2, text="-- REGISTER --",font=("",24,"bold"),bg='gray10',fg="white")
    h1.place(x=280,y=15)
    h2 = Label(root2, text="Name: ",font=("",20,"bold"),bg='gray10',fg="white")
    h2.place(x=60,y=120)
    h3 = Label(root2, text="Password: ",font=("",20,"bold"),bg='gray10',fg="white")
    h3.place(x=60,y=180)
    e1 = Entry(root2,textvariable=nme,font=("",20),width=30)
    e1.place(x=250,y=120)
    e2 = Entry(root2,textvariable=passwrd,font=("",20),width=30)
    e2.place(x=250,y=180)
    h4 = Label(root2, text="Email: ",font=("",20,"bold"),bg='gray10',fg="white")
    h4.place(x=60,y=240)
    h5 = Label(root2, text="Phone No.: ",font=("",20,"bold"),bg='gray10',fg="white")
    h5.place(x=60,y=300)
    e4 = Entry(root2,textvariable=em,font=("",20),width=30)
    e4.place(x=250,y=240)
    e5 = Entry(root2,textvariable=phone,font=("",20),width=30)
    e5.place(x=250,y=300)



    b1 = Button(root2, text="Register",font=("",20,"bold"),bd=2,relief="solid",width=18,command=reg)
    b1.place(x=60,y=400)
    b2 = Button(root2, text="Back To Login",font=("",20,"bold"),bd=2,relief="solid",width=18,command=login)
    b2.place(x=390,y=400)
    root2.mainloop()

signup()
