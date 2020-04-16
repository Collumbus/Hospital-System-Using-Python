import tkinter
import _sqlite3
import tkinter.messagebox

def patient_update():
    rootP = tkinter.Tk()
    rootP.geometry('340x460')
    rootP.title('PATIENT UPDATE FORM:')

    head = tkinter.Label(rootP, text='PATIENT UPDATE FORM:', font='arial 16 bold')

    id = tkinter.Label(rootP, text='PATIENT ID:', font='arial 8 bold', fg='blue')
    patient_id = tkinter.Entry(rootP)

    name = tkinter.Label(rootP, text='PATIENT FULL NAME:', font='arial 8 bold', fg='blue')
    patient_name = tkinter.Entry(rootP)

    sex = tkinter.Label(rootP, text='SEX:', font='arial 8 bold', fg='blue')
    patient_sex = tkinter.Entry(rootP)

    dof = tkinter.Label(rootP, text='DATE OF BIRTH (YYYY-MM-DD):', font='arial 8 bold', fg='blue')
    patient_dof = tkinter.Entry(rootP)

    blood_g = tkinter.Label(rootP, text='BLOOD GROUP:', font='arial 8 bold', fg='blue')
    patient_blood_g = tkinter.Entry(rootP)

    contact1 = tkinter.Label(rootP, text='TELEPHONE:', font='arial 8 bold', fg='blue')
    patient_contact1 = tkinter.Entry(rootP)

    contact2 = tkinter.Label(rootP, text='CONTACT:', font='arial 8 bold', fg='blue')
    patient_contact2 = tkinter.Entry(rootP)

    email = tkinter.Label(rootP, text='E-MAIL:', font='arial 8 bold', fg='blue')
    patient_email = tkinter.Entry(rootP)

    ct = tkinter.Label(rootP, text='CONSULTANT TEAM DOCTOR:', font='arial 8 bold', fg='blue')
    patient_ct = tkinter.Entry(rootP)

    address = tkinter.Label(rootP, text='ADDRESS:', font='arial 8 bold', fg='blue')
    patient_address = tkinter.Entry(rootP)

   # back = tkinter.Button(rootP, text='Back', fg='blue', font='arial 8 bold', bg='orange')
   # search = tkinter.Button(rootP, text='Search', fg='blue', font='arial 8 bold', bg='darkorange')
   # delete = tkinter.Button(rootP, text='Delete', fg='blue', font='arial 8 bold', bg='sienna')
    update = tkinter.Button(rootP, text='Update', fg='blue', font='arial 8 bold', bg='darkmagenta')
   # submit = tkinter.Button(rootP, text='Submit', fg='blue', font='arial 8 bold', bg='darkcyan')


    head.pack()
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

    #submit.pack()
    #back.pack(side=tkinter.LEFT)
    update.pack()
    #delete.pack(side=tkinter.LEFT)
    #search.pack(side=tkinter.LEFT)

    rootP.mainloop()

def patient_delete():
    rootP = tkinter.Tk()
    rootP.geometry('290x150')
    rootP.title('PATIENT DELETE FORM:')

    head = tkinter.Label(rootP, text='INSERT PATIENT ID TO DELETE:', font='arial 8 bold')
    patient_id = tkinter.Entry(rootP)
    delete = tkinter.Button(rootP, text='Delete',  font='arial 8 bold', bg='red')
    head.pack()
    patient_id.pack()
    delete.pack()
    rootP.mainloop()

def patient_search():
    rootP = tkinter.Tk()
    rootP.geometry('400x150')
    rootP.title('PATIENT SEARCH FORM:')

    head = tkinter.Label(rootP, text='INSERT PATIENT TO SEARCH:', font='arial 8 bold')
    patient_id = tkinter.Entry(rootP)
    search = tkinter.Button(rootP, text='Search',  font='arial 8 bold', bg='red')
    head.pack()
    patient_id.pack()
    search.pack()
    rootP.mainloop()
