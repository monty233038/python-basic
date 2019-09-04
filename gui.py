from tkinter import *
import sqlite3
from tkinter import messagebox
gui=Tk()
canvas=Canvas(width=500,height=500,bg='blue')
canvas.pack()
photo = PhotoImage(file='C:\\Users\\mohit\\Desktop\\python\\image3.png')
canvas.create_image(0,0, image=photo,anchor=NW)
gui.title('Registration form')
gui.resizable(width=False,height=False)
gui.geometry('400x400')
fullname = StringVar()
email = StringVar()
gender = StringVar()
mobile = StringVar()
passw = StringVar()
def database_signup():
    name = fullname.get()
    ema = email.get()
    ge = gender.get()
    mb = mobile.get()
    pas = passw.get()
    conn = sqlite3.connect('database.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,Mobile TEXT,Password TEXT)')
    cursor.execute('INSERT INTO Student (Fullname,Email,Gender,Mobile,Password) VALUES(?,?,?,?,?)',(name,ema,ge,mb,pas))
    conn.commit()
    messagebox.showinfo('Done','Signup Successfull')
def database_login():
    conn = sqlite3.connect('database.db')
    new = email.get()
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT Email FROM Student')
        emq = cursor.fetchall()
        for i in emq:
            for j in i:
                veri = j
        if veri == new:
            messagebox.showinfo('Done','Login Successfull')
        else:
            messagebox.showinfo('Error','Login Unsuccessfull')
                    
l0 = Label(gui,text='Registration Form',font=("Bold",10),bg='ghost white',width=20).place(x=100,y=5)
l1 = Label(gui,text='fullname',bd=3,bg='ghost white').place(x=20,y=45)
entry_1 = Entry(gui,width=20,textvar=fullname,fg='red').place(x=80,y=45)
l2 = Label(gui,text='email',bd=3,bg='ghost white').place(x=20,y=80)
entry_2 = Entry(gui,width=20,textvar=email,fg='red').place(x=80,y=80)
l3 = Label(gui,text='password',bd=3,bg='ghost white').place(x=20,y=100)
entry_3 = Entry(gui,width=20,textvar=passw,fg='red',show='*').place(x=80,y=100)
l4 = Label(gui,text='gender',bd=3,bg='ghost white').place(x=20,y=120)
Radiobutton(gui,text='Male',variable=gender,value=1,padx=5,bg='ghost white').place(x=80,y=120)
Radiobutton(gui,text='Female',variable=gender,padx=5,value=2,bg='ghost white').place(x=80,y=140)
Checkbutton(gui,text='Agree to terms&cond.',variable=mobile,bg='ghost white').place(x=20,y=170)
b1 = Button(gui,text='signup',command=database_signup,width=20,bg='ghost white').place(x=50,y=210)
b2 = Button(gui,text='Signin',command=database_login,width=20,bg='ghost white').place(x=170,y=210)
gui.mainloop()