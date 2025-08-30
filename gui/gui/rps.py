import tkinter as tk
import random as rand

userScore = 0
cmpScore = 0
roundNum = 0

def check_winner(userChoice):
    global userScore, cmpScore, roundNum
    youSelected.configure(text="You selected: " + userChoice)
    choices = ["rock", "paper", "scissors"]
    cmpChoice = rand.choice(choices)
    cmpSelected.configure(text="Computer selected: " + cmpChoice)
    if userChoice == cmpChoice:
        pass
    elif userChoice == "rock" and cmpChoice == "scissors":
        userScore += 1
        scoreLabel1.configure(text="Player score: " + str(userScore))
    elif userChoice == "paper" and cmpChoice == "rock":
        userScore += 1
        scoreLabel1.configure(text="Player score: " + str(userScore))
    elif userChoice == "scissors" and cmpChoice == "paper":
        userScore += 1
        scoreLabel1.configure(text="Player score: " + str(userScore))
    else:
        cmpScore += 1
        scoreLabel2.configure(text="Computer score: " + str(cmpScore))
    roundNum += 1

    if roundNum == 10:
        if userScore > cmpScore:
            whoWins.configure(text="Player won!")
        elif cmpScore < userScore:
            whoWins.configure(text="Computer won!")
        elif userScore == cmpScore:
            whoWins.configure(text="Draw!")

screen = tk.Tk()
screen.title("Rock Paper Scissors")
screen.geometry("700x400")

rock = tk.Button(text="Rock",bg="red",width=10,command=lambda:check_winner("rock"))
rock.place(x=100,y=200)
paper = tk.Button(text="Paper",bg="grey",width=10,command=lambda:check_winner("paper"))
paper.place(x=300,y=200)
scissors = tk.Button(text="Scissors",bg="blue",width=10,command=lambda:check_winner("scissors"))
scissors.place(x=500,y=200)

youSelected = tk.Label(text="You selected: ")
youSelected.place(x=200,y=260)
cmpSelected = tk.Label(text="Computer selected: ")
cmpSelected.place(x=200,y=280)
whoWins = tk.Label(fg="green")
whoWins.place(x=330,y=30)

scoreLabel1 = tk.Label(text="Player score: " + str(userScore))
scoreLabel1.place(x=400,y=260)
scoreLabel2 = tk.Label(text="Computer score: " + str(cmpScore))
scoreLabel2.place(x=400,y=280)

print(roundNum)


screen.mainloop()