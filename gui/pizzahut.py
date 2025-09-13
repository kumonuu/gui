import tkinter as tk
from tkinter.ttk import Combobox

screen = tk.Tk()
screen.title("Pizza App")
screen.geometry("800x400")

pizzas = ["Veg Extravaganza", "Hot Honey Pepperoni Feast", "Big New Yorker Margherita", "Cholula Chicken Sizzler", "The Meaty One"]

favPizza = tk.StringVar()
pizzaMenu = Combobox(screen,textvariable=favPizza,values=pizzas,state="readonly")
pizzaMenu.set("Select a pizza")
pizzaMenu.place(x=400,y=200)

size = tk.StringVar()
size.set("Medium Size")
small = tk.Radiobutton(screen,text="S",variable=size,value="Small Size")
small.place(x=600,y=195)
medium = tk.Radiobutton(screen,text="M",variable=size,value="Medium Size")
medium.place(x=600,y=215)
large = tk.Radiobutton(screen,text="L",variable=size,value="Large Size")
large.place(x=600,y=235)

screen.mainloop()