import tkinter


def Entry():
    global userbox, passbox, login, topframe, bottomframe, image_1
    root = tkinter.Tk()
    root.geometry('280x250')
    topframe = tkinter.Frame(root)
    topframe.pack()

    bottomframe = tkinter.Frame(root)
    bottomframe.pack()

    heading = tkinter.Label(topframe, text = 'Hospital System', bg = 'white', fg = 'green', font = 'Times 16 bold italic')

    username = tkinter.Label(topframe, text = 'User:')
    userbox = tkinter.Entry(topframe)

    password = tkinter.Label(bottomframe, text = 'Password:')
    passbox = tkinter.Entry(bottomframe)

    login = tkinter.Button(bottomframe, text = 'LOGIN', font = 'arial 8 bold')

    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title('Hospital System : LOGIN :')
    root.mainloop()

Entry()
