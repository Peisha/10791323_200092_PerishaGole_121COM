from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import os,glob
import mysql.connector
from mysql.connector import Error

 
 
#creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.configure(bg="light blue")
        self.title("LIBRARY MANAGEMENT SYSTEM")
 

#verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD" )
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='1234')
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admin` where user= %s AND password = %s ',(user,password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'options.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")

        def check():


                    self.label = Label(self, text="LOGIN" , fg = 'black', font=("times new roman", 20,'bold'))
                    self.label.place(x=550, y=90)
                    self.label1 = Label(self, text="User-Name :" , fg = 'black', font=("times new roman", 30, 'bold'))
                    self.label1.place(x=270, y=180)
                    self.user_text = Entry(self, textvariable=self.a, width=45)
                    self.user_text.place(x=600, y=180, height='50')
                    self.label2 = Label(self, text="Password :"  , fg = 'black', font=("times new roman", 30, 'bold'))
                    self.label2.place(x=270, y=280)
                    self.pass_text = Entry(self, show='*', textvariable=self.b, width=45)
                    self.pass_text.place(x=600, y=280, height='50')
                    self.butt = Button(self, text="Login",bg ='red', font=30, width=20, command=chex).place(x=500, y=400)
                    self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM", fg='black', font=("times new roman", 30, 'bold'))
                    self.label3.place(x=300, y=30)


        check()

Lib().mainloop()
