import tkinter

def patient_bill():
    rootB = tkinter.Tk()
    rootB.geometry('450x350')
    rootB.title('BILLING FORM')
    head = tkinter.Label(rootB, text='PATIENT BILLS', font='arial 16 bold italic', fg='orange')
    head.place(x=100, y=10)

    id = tkinter.Label(rootB, text='PATIENT ID:')
    id.place(x=20, y=60)

    patient_id =tkinter.Entry(rootB)
    patient_id.place(x=100, y=60)

    date_l = tkinter.Label(rootB, text='DATE:')
    date_l.place(x=20, y=100)

    dd =tkinter.Entry(rootB)
    dd.place(x=135, y=100)

    dd_update = tkinter.Button(rootB, text='UPDATE DATE')
    dd_update.place(x=270, y=100)

    treat = tkinter.Label(rootB, text='TYPE OF TREATMENT')
    treat.place(x=20, y=140)

    # We must create a lisbox here!

    cost_l = tkinter.Label(rootB, text='COST:')
    cost_l.place(x=315, y=140)

    cost_t = tkinter.Entry(rootB, width=5)
    cost_t.place(x=350, y=140)

    med_l = tkinter.Label(rootB, text='SELECT MEDICINE:')
    med_l.place(x=20, y=180)

    med_ql = tkinter.Label(rootB, text='AMOUNT:')
    med_ql.place(x=20, y=180)

    price_l = tkinter.Label(rootB, text='PRICE:')
    price_l.place(x=315, y=180)

    price = tkinter.Entry(rootB, width=5)
    price.place(x=360, y=180)
