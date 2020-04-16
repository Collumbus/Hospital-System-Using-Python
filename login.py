import tkinter
from menu import menu

root = None
userbox  = None
passbox = None
topframe = None
bottomframe = None
frame3 = None
login = None

def get_login():
    global userbox, passbox, error
    usertest = userbox.get()
    passwordtest = passbox.get()
    if (usertest == 'master' and passwordtest == 'master'):
        root.destroy()
        menu()
    else:
        error = tkinter.Label(bottomframe, text='PLEASE ENTER A VALID USERNAME AND PASSWORD!', fg='red', font='bold')
        error.pack()

def entry():
    global root, userbox, passbox, login, topframe, bottomframe, image_1
    root = tkinter.Tk()
    root.geometry('440x480')
    topframe = tkinter.Frame(root)
    topframe.pack()

    bottomframe = tkinter.Frame(root)
    bottomframe.pack()

    head = tkinter.Label(topframe, width=45, text='Hospital System', bg='#135823', fg='grey', font='Times 16 bold ' 'italic')

    username = tkinter.Label(topframe, text='User:')
    userbox = tkinter.Entry(topframe)

    password = tkinter.Label(bottomframe, text='Password:')
    passbox = tkinter.Entry(bottomframe)

    login = tkinter.Button(bottomframe, text='LOGIN', font='arial 8 bold', command=get_login)
    root.wm_iconbitmap(r'D:\\DataScience\\Hospital-System-Using-Python\\icons\\password.ico')
    image = tkinter.PhotoImage(file='D:\\DataScience\\Hospital-System-Using-Python\\img\\login.png')
    image = image.subsample(1,1)
    labelimg = tkinter.Label(image=image, height='380', width='300')
    labelimg.pack()

    head.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title('Hospital System : LOGIN :')
    root.mainloop()


entry()
