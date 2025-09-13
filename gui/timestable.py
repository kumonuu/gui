import tkinter as tk
from tkinter.ttk import Combobox

screen = tk.Tk()
screen.title("Times Table")
screen.geometry("500x700")

table = tk.Label(text="")
table.place(x=220,y=100)

def generate_table():
    global tableStore
    tableStore = ""
    num = numberBox.get()
    num2 = numberBox2.get()
    for i in range(num2+1):
        tableStore += str(num) + " x " + str(i) + " = " + str(num*i) + "\n"
    table.configure(text=tableStore)
    
numList = []
for i in range(30):
    numList.append(i+1)

prompt = tk.Label(text="Number:")
prompt.place(x=90,y=50)

numberBox = tk.IntVar()
numberMenu = Combobox(screen,textvariable=numberBox,values=numList,state="readonly")
numberMenu.place(x=180,y=50)
numberMenu.set("Select a number")

numberBox2 = tk.IntVar()
numberOption = tk.Radiobutton(screen,text="10",variable=numberBox2,value=10)
numberOption.place(x=360,y=80)
numberOption2 = tk.Radiobutton(screen,text="20",variable=numberBox2,value=20)
numberOption2.place(x=360,y=100)
numberOption3 = tk.Radiobutton(screen,text="30",variable=numberBox2,value=30)
numberOption3.place(x=360,y=120)
numberBox2.set(10)

genButton = tk.Button(text="Generate", command=generate_table)
genButton.place(x=90,y=80)

screen.mainloop()