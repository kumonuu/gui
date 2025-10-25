import tkinter as tk
from tkinter import messagebox

screen = tk.Tk()
screen.title("Jumbled word game")
screen.geometry("500x500")

words = ["","","","",""]

def jumble():
    pass

frame = tk.Frame(screen,bg="black",width=500,height=500)
frame.place(x=0,y=0)
title = tk.Label(frame,text="JUMBLED WORD GAME",bg="black",fg="white",font="bold,140")
title.place(x=120,y=10)

text_input = tk.Text(frame,width=25,height=3)
text_input.place(x=150,y=150)

screen.mainloop()