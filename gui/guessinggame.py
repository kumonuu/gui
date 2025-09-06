import tkinter as tk
from tkinter import messagebox
import random as rand

screen = tk.Tk()
screen.title("Guessing Game")
screen.geometry("500x500")
randNum = rand.randint(1,20)

def show_msg():
    name = nameBox.get()
    msgBox = messagebox.showinfo("Name","Well, " + name + ", I am thinking of a number between 1 and 20.")

def check_answer():
    inputNum = int(guessInput.get())
    if inputNum > randNum:
        msgBox = messagebox.showerror("High guess!","Your guess is too high, enter a smaller number.")
    elif inputNum < randNum:
        msgBox = messagebox.showerror("Low guess!","Your guess is too low, enter a bigger number.")
    else:
        msgBox = messagebox.showinfo("Correct!","Well done, you guessed it right. Good job!")

question = tk.Label(text="What's your name?")
question.place(x=40,y=40)
nameBox = tk.Entry(screen)
nameBox.place(x=40,y=60)
okButton = tk.Button(text="OK",command=show_msg)
okButton.place(x=350,y=55)
prompt = tk.Label(text="Take a guess:")
prompt.place(x=40,y=150)
guessInput = tk.Entry(screen)
guessInput.place(x=130,y=150)
guessButton = tk.Button(text="Guess", command=check_answer)
guessButton.place(x=350,y=145)

screen.mainloop()