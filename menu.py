import tkinter
import sqlite3
import tkinter.messagebox
from patient_reg import patient_reg
from employee_reg import employee_reg
from patient_bill import  patient_bill

def menu():
    global root1, button1, button2, button3, button4, button5, button6

    root1 = tkinter.Tk()
    root1.geometry('280x350')
    root1.title('Hospital System : MENU :')
    m = tkinter.Label(root1, text='MENU', font='Times 16 bold ' 'italic', fg='grey')
    button1 = tkinter.Button(root1, text='REGISTER PACIENT:', bg='light blue', fg='black', command=patient_reg)
    button2 = tkinter.Button(root1, text='ROOM-N:', bg='light green', fg='black')
    button3 = tkinter.Button(root1, text='EMPLOYEE REGISTRATION:', bg='light blue', fg='black', command=employee_reg)
    button4 = tkinter.Button(root1, text='RESERVATIONS:', bg='light green', fg='black')
    button5 = tkinter.Button(root1, text='PATIENT BILLING:', bg='light blue', fg='black', command=patient_bill)
    button6 = tkinter.Button(root1, text='EXIT:', bg='light green', fg='black')

    m.place(x=75, y=5)
    button1.pack(side=tkinter.TOP)
    button1.place(x=80, y=50)

    button2.pack(side=tkinter.TOP)
    button2.place(x=80, y=100)

    button3.pack(side=tkinter.TOP)
    button3.place(x=80, y=150)

    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=200)

    button5.pack(side=tkinter.TOP)
    button5.place(x=80, y=250)

    button6.pack(side=tkinter.TOP)
    button6.place(x=80, y=300)
    root1.mainloop()


