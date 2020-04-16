import tkinter

def room_details():
    rootRD = tkinter.Tk()
    rootRD.geometry('280x280')
    rootRD.title('ROOM INFORMATION')

    head = tkinter.Label(rootRD, text='Patient ID', font='Times 13 bold', fg='orange')
    head.place(x=20, y=20)

    patient_id = tkinter.Entry(rootRD)
    patient_id.place(x=50, y=50)

    search = tkinter.Button(rootRD, text='Search', font='Times 8 bold', fg='orange')
    search.place(x=70, y=80)

    exit = tkinter.Button(rootRD, text='Exit', font='Times 8 bold', fg='orange')
    exit.place(x=150, y=80)

    rootRD.mainloop()

def room_finder():
    rootR = tkinter.Tk()
    rootR.geometry('400x400')
    rootR.title('FIND ROOM:')
    head = tkinter.Label(rootR, text='FIND ROOM:', font='Times 13 bold', fg='orange')
    head.place(x=75, y=10)

    id = tkinter.Label(rootR, text='PATIENT ID:', font='Times 8 bold', fg='orange')
    id.place(x=30, y=60)

    patient_id = tkinter.Entry(rootR)
    patient_id.place(x=100, y=60)

    room_tl = tkinter.Label(rootR, text='ROOM TYPE:', font='Times 8 bold', fg='orange')
    room_tl.place(x=30, y=100)

    rate_l = tkinter.Label(rootR, text='ROOM RATE:', font='Times 8 bold', fg='orange')
    rate_l.place(x=30, y=220)

    rate = tkinter.Entry(rootR)
    rate.place(x=130, y=220)

    ed_l = tkinter.Label(rootR, text='ENTRY DATE:', font='Times 8 bold', fg='orange')
    ed_l.place(x=30, y=260)

    ed = tkinter.Entry(rootR)
    ed.place(x=140, y=260)

    dd_l = tkinter.Label(rootR, text='DEPARTURE DATE:', font='Times 8 bold', fg='orange')
    dd_l.place(x=30, y=300)

    dd = tkinter.Entry(rootR)
    dd.place(x=155, y=300)

    submit = tkinter.Button(rootR, text='Submit', font='Times 8 bold', fg='orange')
    submit.place(x=30, y=340)

    update = tkinter.Button(rootR, text='Update', font='Times 8 bold', fg='orange')
    update.place(x=130, y=340)

    room_d = tkinter.Button(rootR, text='Room Details', font='Times 8 bold', fg='orange', command=room_details)
    room_d.place(x=220, y=340)

    exit = tkinter.Button(rootR, text='Exit', font='Times 8 bold', fg='orange')
    exit.place(x=330, y=340)

    rootR.mainloop()
