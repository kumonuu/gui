import tkinter as tk
import random as rd
from tkinter import messagebox

screen = tk.Tk()
screen.title("Jumbled word game")
screen.geometry("500x500")

words = ["discipline","complex","shareholder","cemetery","basketball"]
jumbled_words = []
score = 0

def choose_word():
    return rd.choice(words)

def jumble(word):
    random_word = rd.sample(word,len(word))
    jumbled = "".join(random_word)
    return jumbled

def check():
    global jumbled_word, score
    text_value = text_input.get(1.0,tk.END)
    text_value = text_value.strip()
    index = jumbled_words.index(jumbled_word)
    if text_value == words[index]:
        print("Correct answer")
        score += 1
        score_display.configure(text="Score: " + str(score))
    else:
        print("Incorrect answer")
        score -= 1
        score_display.configure(text="Score: " + str(score))
    words.pop(index)
    jumbled_words.pop(index)
    if jumbled_words:
        jumbled_word = rd.choice(jumbled_words)
        word_display.configure(text=jumbled_word)
    else:
        print("Game over")
        word_display.configure(text="Game over\nYou scored " + str(score) + " points")
        check_btn.configure(state='disabled')

for word in words:
    jumbled_word = jumble(word)
    jumbled_words.append(jumbled_word)

jumbled_word = rd.choice(jumbled_words)

frame = tk.Frame(screen,bg="black",width=500,height=500)
frame.place(x=0,y=0)
title = tk.Label(frame,text="JUMBLED WORD GAME",bg="black",fg="white",font="bold,140")
title.place(x=140,y=10)

text_input = tk.Text(frame,width=25,height=3)
text_input.place(x=150,y=150)

word_display = tk.Label(frame,bg="black",fg="white",font="bold,40",text=jumbled_word)
word_display.place(x=165,y=70)

score_display = tk.Label(frame,bg="black",fg="white",font="bold,40",text="Score: " + str(score))
score_display.place(x=10,y=470)

check_btn = tk.Button(frame,width=10,height=1,text="Check",command=check)
check_btn.place(x=200,y=240)

screen.mainloop()