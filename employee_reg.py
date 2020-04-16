import tkinter

def employee_reg():
    rootE = tkinter.Tk()
    rootE.title('EMPLOYEES REGISTRATION FORM:')
    rootE.geometry('400x400')

    var = tkinter.StringVar(master=rootE)

    head = tkinter.Label(rootE, text='REGISTER EMPLOYEES:', fg='grey', font='arial 10 bold')
    head.place(x=50, y=20)

    l1 = tkinter.Label(rootE, text='EMPLOYEES ID:', fg='green', font='arial 8 bold')
    l1.place(x=50, y=50)

    t1 = tkinter.Entry(rootE)
    t1.place(x=170, y=50)

    l2 = tkinter.Label(rootE, text='EMPLOYEE NAME:', fg='green', font='arial 8 bold')
    l2.place(x=50, y=80)

    t2 = tkinter.Entry(rootE)
    t2.place(x=170, y=80)

    l3 = tkinter.Label(rootE, text='SEX:', fg='green', font='arial 8 bold')
    l3.place(x=50, y=110)

    # we have to create an variable
    r1 = tkinter.Radiobutton(rootE, text='MALE', value='male')
    r1.place(x=80, y=110)

    r2 = tkinter.Radiobutton(rootE, text='FEMALE', value='female')
    r2.place(x=150, y=110)

    l4 = tkinter.Label(rootE, text='AGE:', fg='green', font='arial 8 bold')
    l4.place(x=50, y=140)

    t3 = tkinter.Entry(rootE)
    t3.place(x=80, y=140)

    l5 = tkinter.Label(rootE, text='EMPLOYEE POSITION:', fg='green', font='arial 8 bold')
    l5.place(x=50, y=170)

    scrollbar = tkinter.Scrollbar(rootE, width=15)
    scrollbar.place(x=310, y=155)

    lb = tkinter.Listbox(rootE, selectmode='SINGLE', exportselection=0, height=1, width=21)
    lb.insert(tkinter.END, 'DOCTOR')
    lb.insert(tkinter.END, 'NURSE')
    lb.insert(tkinter.END, 'NURSING TECHNICIAN')
    lb.place(x=170, y=170)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lb.yview)

    l6 = tkinter.Label(rootE, text='SALARY:', fg='green', font='arial 8 bold')
    l6.place(x=50, y=200)

    t4 = tkinter.Entry(rootE)
    t4.place(x=110, y=200)

    l7 = tkinter.Label(rootE, text='EXPERIENCE:', fg='green', font='arial 8 bold')
    l7.place(x=50, y=230)

    t5 = tkinter.Entry(rootE)
    t5.place(x=140, y=200)

    l8 = tkinter.Label(rootE, text='TELEPHONE:', fg='green', font='arial 8 bold')
    l8.place(x=50, y=260)

    t6 = tkinter.Entry(rootE)
    t6.place(x=140, y=260)

    l9 = tkinter.Label(rootE, text='E-MAIL:', fg='green', font='arial 8 bold')
    l9.place(x=50, y=290)

    t7 = tkinter.Entry(rootE)
    t7.place(x=90, y=290)

    rootE.mainloop()
