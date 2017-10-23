import tkinter
from tkinter import *
import sqlite3
from tkinter import messagebox

conn=sqlite3.connect('gui.sqlite')
cur=conn.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS User(
            name TEXT,
            age TEXT,
            gender TEXT,
            address TEXT)
            ''')

mw=tkinter.Tk()

def save():
    n=e1.get()
    a=age.get()
    a=str(a)
    g=b.get()
    ad=e2.get()


    messagebox.showinfo('YOUR INFO','Name: '+n+'\nAge: '+a+'\nGender: '+g+'\nAddress: '+ad)

    cur.execute('INSERT OR REPLACE INTO User(name,age,gender,address) VALUES (?,?,?,?)',(n,a,g,ad))

    conn.commit()

b=StringVar()

Label(mw,text='Name:').grid(row=0,column=0)
e1=Entry(mw)
e1.grid(row=0,column=1)
Label(mw,text='Age:').grid(row=1,column=0)
age=Scale(mw,from_=1,to=100,orient='horizontal',length=200)
age.grid(row=1,column=1)
Label(mw,text='Gender:').grid(row=2,column=0)
Radiobutton(mw,text='Male',value='Male',variable=b).grid(row=2,column=1)
Radiobutton(mw,text='Female',value='Female',variable=b).grid(row=3,column=1)
Label(mw,text='Address:').grid(row=4,column=0)
e2=Entry(mw,width=40)
e2.grid(row=5,column=1)

Button(mw,text='Done',command=save).grid(row=6,column=0)
Button(mw,text='Close',command=mw.destroy).grid(row=6,column=1)

mainloop()
