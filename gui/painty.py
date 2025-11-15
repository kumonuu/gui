import tkinter as tk

screen = tk.Tk()
screen.title("Painty")
screen.geometry("500x500")

canvas = tk.Canvas(screen,bg="white",width=400,height=400)
canvas.grid(row=30,column=30,padx=50,pady=50)
canvas.create_oval(70,70,90,90,fill="green")

screen.mainloop()