import tkinter, calendar

def test():
    cl = calendar.calendar(int(entry.get()))
    print(cl)
    clscreen = tkinter.Tk()
    clscreen.title("Calendar")
    clscreen.geometry('300x300')

    cldisplay = tkinter.Text(clscreen,width=100,height=100,fg="red")
    cldisplay.pack(side='left')
    cldisplay.insert(tkinter.END,chars=cl)

    scrollbar = tkinter.Scrollbar(clscreen,command=cldisplay.yview)
    scrollbar.pack(side='right',fill='y')
    cldisplay.config(yscrollcommand=scrollbar.set)

screen = tkinter.Tk()
screen.title("App")
screen.geometry('1000x500')

entry = tkinter.Entry(screen)
entry.place(x=50,y=50)
#entry.grid(row=0,column=1)
#entry.pack(anchor='center')

label = tkinter.Label(screen, text="Year",fg="red")
label.place(x=10,y=50)

button = tkinter.Button(screen, text="Submit", cursor='hand2', command=test)
button.place(x=50,y=70)

screen.mainloop()
