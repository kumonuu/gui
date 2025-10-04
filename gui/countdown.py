import tkinter as tk
import time
from tkinter import messagebox

def set_countdown():
    button["state"] = "disabled"
    second = secsvar.get()
    minute = minsvar.get()
    hour = hoursvar.get()

    hours.configure(state="readonly")
    mins.configure(state="readonly")
    secs.configure(state="readonly")

    second = int(second)
    minuteAsSecond = int(minute) * 60
    hourAsSecond = int(hour) * 3600
    totalTime = hourAsSecond + minuteAsSecond + second
    while totalTime > 0:
        time.sleep(1)
        totalTime -= 1
        minute, second = divmod(totalTime,60)
        hour, minute = divmod(minute,60)
        hoursvar.set('{:02d}'.format(hour))
        minsvar.set('{:02d}'.format(minute))
        secsvar.set('{:02d}'.format(second))
        screen.update()
    messagebox.showinfo("Time's up!", "The timer has reached zero.")

screen = tk.Tk()
screen.title("Countdown")
screen.geometry("500x500")

hoursvar = tk.StringVar()
hoursvar.set("00")
hours = tk.Entry(screen,width=3,textvariable=hoursvar)
hours.place(x=50,y=50)

minsvar = tk.StringVar()
minsvar.set("00")
mins = tk.Entry(screen,width=3,textvariable=minsvar)
mins.place(x=70,y=50)

secsvar = tk.StringVar()
secsvar.set("00")
secs = tk.Entry(screen,width=3,textvariable=secsvar)
secs.place(x=90,y=50)

button = tk.Button(screen,text="Set Time Countdown",command=set_countdown)
button.place(x=50,y=80)

screen.mainloop()