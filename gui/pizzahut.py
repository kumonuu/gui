import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

screen = tk.Tk()
screen.title("Pizza App")
screen.geometry("800x400")
frame = tk.Frame(screen,bg="pink",bd=30)
innerFrame = tk.Frame(screen,bd=50)
frame.pack(fill='both',expand=True)
innerFrame.place(x=60,y=60,relwidth=0.7,relheight=0.7)

pizzas = ["Veg Extravaganza", "Hot Honey Pepperoni Feast", "Big New Yorker Margherita", "Cholula Chicken Sizzler", "The Meaty One"]
nums = []

for i in range(1,11):
    nums.append(i)

orderLabel = tk.Label(innerFrame,text="")
orderLabel.place(x=350,y=325)

def show_order():
    num = quantity.get()
    pizza = favPizza.get()
    pizzaSize = size.get()
    if pizza == "Select a pizza":
        msgBox = messagebox.showwarning("No pizza selected","Please select a pizza from the menu.")
    else:
        orderText = "You ordered " + str(num) + " " + pizza + " " + pizzaSize + " Pizza(s)"
        orderLabel.configure(text=orderText)

favPizza = tk.StringVar()
pizzaMenu = Combobox(innerFrame,textvariable=favPizza,values=pizzas,state="readonly")
pizzaMenu.set("Select a pizza")
pizzaMenu.place(x=400,y=200)

quantity = tk.IntVar()
quantityMenu = Combobox(innerFrame,textvariable=quantity,values=nums,state="readonly")
quantityMenu.set(1)
quantityMenu.place(x=400,y=230)

size = tk.StringVar()
size.set("Medium Size")
small = tk.Radiobutton(innerFrame,text="S",variable=size,value="Small Size")
small.place(x=600,y=195)
medium = tk.Radiobutton(innerFrame,text="M",variable=size,value="Medium Size")
medium.place(x=600,y=215)
large = tk.Radiobutton(innerFrame,text="L",variable=size,value="Large Size")
large.place(x=600,y=235)

order = tk.Button(innerFrame,text="Order",command=show_order)
order.place(x=450,y=265)

screen.mainloop()