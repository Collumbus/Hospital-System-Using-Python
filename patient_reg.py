import tkinter

def patient_reg():
    rootP = tkinter.Tk()
    rootP.geometry('340x460')
    rootP.title('PATIENT REGISTRATION FORM:')

    head = tkinter.Label(rootP, text='PATIENT REGISTRATION FORM:', font='arial 16 bold')

    id = tkinter.Label(rootP, text='PATIENT ID:', font='arial 8 bold', fg='blue')
    patient_id = tkinter.Entry(rootP, width=12)

    name = tkinter.Label(rootP, text='PATIENT FULL NAME:', font='arial 8 bold', fg='blue')
    patient_name = tkinter.Entry(rootP, width=50)

    sex = tkinter.Label(rootP, text='SEX:', font='arial 8 bold', fg='blue')
    patient_sex = tkinter.Entry(rootP, width=10)

    dof = tkinter.Label(rootP, text='DATE OF BIRTH (YYYY-MM-DD):', font='arial 8 bold', fg='blue')
    patient_dof = tkinter.Entry(rootP, width=26)

    blood_g = tkinter.Label(rootP, text='BLOOD GROUP:', font='arial 8 bold', fg='blue')
    patient_blood_g = tkinter.Entry(rootP, width=26)

    contact1 = tkinter.Label(rootP, text='TELEPHONE:', font='arial 8 bold', fg='blue')
    patient_contact1 = tkinter.Entry(rootP, width=26)

    contact2 = tkinter.Label(rootP, text='CONTACT:', font='arial 8 bold', fg='blue')
    patient_contact2 = tkinter.Entry(rootP, width=26)

    email = tkinter.Label(rootP, text='E-MAIL:', font='arial 8 bold', fg='blue')
    patient_email = tkinter.Entry(rootP, width=50)

    ct = tkinter.Label(rootP, text='CONSULTANT TEAM DOCTOR:', font='arial 8 bold', fg='blue')
    patient_ct = tkinter.Entry(rootP, width=30)

    address = tkinter.Label(rootP, text='ADDRESS:', font='arial 8 bold', fg='blue')
    patient_address = tkinter.Entry(rootP, width=50)

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

    rootP.mainloop()
