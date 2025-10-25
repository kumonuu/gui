import tkinter as tk
import speech_recognition as sr
from tkinter.filedialog import *
from tkinter import messagebox

screen = tk.Tk()
screen.title("Speech to Text")
screen.geometry("800x400")

def record():
    recognizer = sr.Recognizer()
    with sr.Microphone() as microphone:
        audio = recognizer.listen(microphone)
        try:
            converted_text = recognizer.recognize_google(audio)
        except Exception as e:
            converted_text = "Sorry! Encountered an error"
            print(e)
        text_input.delete(1.0,tk.END)
        text_input.insert(tk.END,converted_text)

def save():
    text = text_input.get(1.0,tk.END)
    try:
        file = asksaveasfilename(defaultextension='.txt')
        if file.endswith('.py'):
            raise ValueError("Wrong file extension")
    except ValueError as e:
        messagebox.showerror("Bad file","Could not save file: " + str(e))
        print(e)
    print(text,file=file)
        

title = tk.Label(screen,text="Voice Notepad",font="bold,20")
title.place(x=320,y=50)

text_input = tk.Text(screen,width=30,height=5)
text_input.place(x=290,y=200)

save_btn = tk.Button(screen,text="Save the Text",width=20,command=save)
save_btn.place(x=550,y=200)

record_btn = tk.Button(screen,text="Click on me!..\nTo start recording",command=record)
record_btn.place(x=160,y=200)

screen.mainloop()