import tkinter as tk
import os
from gtts import gTTS

screen = tk.Tk()
screen.title("Text to Speech Converter")
screen.geometry("800x500")

def convert():
    gtts = gTTS(text_input.get(),lang="en",slow=False)
    gtts.save("audio.mp3")
    os.system("audio.mp3")

title = tk.Label(screen,text="Text to Speech",font="bold,20")
title.place(x=340,y=210)

text_input = tk.Entry(screen,width=40,bd=5)
text_input.place(x=290,y=250)

submit_btn = tk.Button(screen,text="SUBMIT",bg="yellow",bd=3,command=convert).place(x=390,y=300)

screen.mainloop()