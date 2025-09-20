import tkinter as tk
from datetime import datetime

screen = tk.Tk()
screen.title("Digital Timer")
screen.geometry("500x500")


label = tk.Label(screen,text="")
label.place(x=220,y=250)

def update_time():
    time = datetime.now()
    currentTime = time.strftime('%I:%M:%S %p')
    label.configure(text=currentTime)
    label.after(1000,update_time)

update_time()

screen.mainloop()