import tkinter

def reservation():
    rootR = tkinter.Tk()
    rootR.geometry('500x550')
    rootR.title('Reservation')
    head = tkinter.Label(rootR, text='Reservation', fg='blue', font='arial 10 bold')
    head.place(x=55, y=5)

    p_id = tkinter.Label(rootR, text='Patient ID', fg='blue', font='arial 8 bold')
    p_id.place(x=20, y=30)

    patient_id = tkinter.Entry(rootR)
    patient_id.place(x=100, y=30)

    d_id = tkinter.Label(rootR, text='Doctor ID', fg='blue', font='arial 8 bold')
    d_id.place(x=20, y=60)

    doctor_id = tkinter.Entry(rootR)
    doctor_id.place(x=110, y=60)

    r_id = tkinter.Label(rootR, text='Reservation Nº', fg='blue', font='arial 8 bold')
    r_id.place(x=20, y=90)

    r_time = tkinter.Label(rootR, text='Reservation Time (HH:MM:SS)', fg='blue', font='arial 8 bold')
    r_time.place(x=20, y=120)

    re_time = tkinter.Entry(rootR)
    re_time.place(x=20, y=145)

    r_date = tkinter.Label(rootR, text='Reservation Date (YYYY-MM-DD)', fg='blue', font='arial 8 bold')
    r_date.place(x=20, y=170)

    re_date = tkinter.Entry(rootR)
    re_date.place(x=20, y=195)

    description = tkinter.Label(rootR, text='Description', fg='blue', font='arial 8 bold')
    description.place(x=20, y=220)

    description_e = tkinter.Text(rootR, width=20, height=3)
    description_e.place(x=20, y=245)

    reserve = tkinter.Button(rootR, text='Generate', fg='blue', font='arial 8 bold')
    reserve.place(x=20, y=310)

    delete = tkinter.Button(rootR, text='Delete', fg='blue', font='arial 8 bold')
    delete.place(x=180, y=310)

    reservations = tkinter.Button(rootR, text='Reservations', fg='blue', font='arial 8 bold')
    reservations.place(x=320, y=310)

    rootR.mainloop()
