import tkinter
import sqlite3
import tkinter.messagebox

def menu():
    global root1, button1, button2, button3, button4, button5, button6

    root1 = tkinter.Tk()
    root1.geometry('280x350')
    root1.title('Hospital System : MENU :')
    m = tkinter.Label(root1, text='MENU', font='Times 16 bold ' 'italic', fg='grey')
    button1 = tkinter.Button(root1, text='REGISTER PACIENT:', bg='light blue', fg='black', command=patient)
    button2 = tkinter.Button(root1, text='ROOM-N:', bg='light green', fg='black')
    button3 = tkinter.Button(root1, text='EMPLOYEE REGISTRATION:', bg='light blue', fg='black')
    button4 = tkinter.Button(root1, text='RESERVATIONS:', bg='light green', fg='black')
    button5 = tkinter.Button(root1, text='PATIENT ACCOUNT:', bg='light blue', fg='black')
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

def patient():
    rootp = tkinter.Tk()
    rootp.geometry('340x460')
    rootp.title('PATIENT REGISTRATION FORM:')

    regform = tkinter.Label(rootp, text='PATIENT REGISTRATION FORM:', font='arial 16 bold')

    id = tkinter.Label(rootp, text='PATIENT ID:', font='arial 8 bold', fg='blue')
    patient_id = tkinter.Entry(rootp, width=12)

    name = tkinter.Label(rootp, text='PATIENT FULL NAME:', font='arial 8 bold', fg='blue')
    patient_name = tkinter.Entry(rootp, width=50)

    sex = tkinter.Label(rootp, text='SEX:', font='arial 8 bold', fg='blue')
    patient_sex = tkinter.Entry(rootp, width=10)

    dof = tkinter.Label(rootp, text='DATE OF BIRTH (YYYY-MM-DD):', font='arial 8 bold', fg='blue')
    patient_dof = tkinter.Entry(rootp, width=26)

    blood_g = tkinter.Label(rootp, text='BLOOD GROUP:', font='arial 8 bold', fg='blue')
    patient_blood_g = tkinter.Entry(rootp, width=26)

    contact1 = tkinter.Label(rootp, text='TELEPHONE:', font='arial 8 bold', fg='blue')
    patient_contact1 = tkinter.Entry(rootp, width=26)

    contact2 = tkinter.Label(rootp, text='CONTACT:', font='arial 8 bold', fg='blue')
    patient_contact2 = tkinter.Entry(rootp, width=26)

    email = tkinter.Label(rootp, text='E-MAIL:', font='arial 8 bold', fg='blue')
    patient_email = tkinter.Entry(rootp, width=50)

    ct = tkinter.Label(rootp, text='CONSULTANT TEAM DOCTOR:', font='arial 8 bold', fg='blue')
    patient_ct = tkinter.Entry(rootp, width=30)

    address = tkinter.Label(rootp, text='ADDRESS:', font='arial 8 bold', fg='blue')
    patient_address = tkinter.Entry(rootp, width=50)

    regform.pack()
    id.pack()
    patient_id.pack()
    name.pack()
    patient_name.pack()
    sex.pack()
    patient_sex.pack()
    dof.pack()
    patient_dof.pack()
    blood_g.pack()
    patient_blood_g.pack()
    contact1.pack()
    patient_contact1.pack()
    contact2.pack()
    patient_contact2.pack()
    email.pack()
    patient_email.pack()
    ct.pack()
    patient_ct.pack()
    address.pack()
    patient_address.pack()

    rootp.mainloop()
