import tkinter as tk
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk

screen = tk.Tk()
screen.title("Painty")
screen.geometry("500x500")

active_btn = None
x = None
y = None
btn_size = (20,20)

def pen():
    activate(pen_btn)

def brush():
    activate(brush_btn)
    print(active_btn.cget("text"))

def color():
    global color
    color = askcolor(color=color)[1]

def eraser():
    activate(eraser_btn)
    print(active_btn.cget("text"))

def reset(event):
    global x, y
    x = None
    y = None

scale = tk.Scale(screen,from_=0,to=10,orient="horizontal")
scale.place(x=390,y=10)

def paint(event):
    global x, y
    if x and y:
        if active_btn == pen_btn:
            canvas.create_line(x,y,event.x,event.y,fill=color,smooth=True,capstyle="round",width=scale.get())
        elif active_btn == brush_btn:
            canvas.create_line(x,y,event.x,event.y,fill=color,smooth=True,capstyle="round",width=scale.get()+10)
        elif active_btn == eraser_btn:
            canvas.create_line(x,y,event.x,event.y,fill="white",smooth=True,capstyle="round",width=scale.get())
    x = event.x
    y = event.y

def activate(btn):
    global active_btn
    active_btn.config(relief="raised")
    btn.config(relief="sunken")
    active_btn = btn
    print("button activated")
    
canvas = tk.Canvas(screen,bg="white",width=400,height=400)
canvas.grid(row=30,column=30,padx=50,pady=50)

pen_img = Image.open("pencil.png").resize(btn_size)
pen_img = ImageTk.PhotoImage(pen_img)
brush_img = Image.open("brush.png").resize(btn_size)
brush_img = ImageTk.PhotoImage(brush_img)
color_img = Image.open("color.png").resize(btn_size)
color_img = ImageTk.PhotoImage(color_img)
eraser_img = Image.open("eraser.png").resize(btn_size)
eraser_img = ImageTk.PhotoImage(eraser_img)
    
pen_btn = tk.Button(screen,image=pen_img,command=pen)
pen_btn.place(x=30,y=10)
brush_btn = tk.Button(screen,image=brush_img,command=brush)
brush_btn.place(x=120,y=10)
color_btn = tk.Button(screen,image=color_img,command=color)
color_btn.place(x=210,y=10)
eraser_btn = tk.Button(screen,image=eraser_img,command=eraser)
eraser_btn.place(x=300,y=10)

def init():
    global active_btn
    global color
    color = "black"
    active_btn = pen_btn
    canvas.bind('<B1-Motion>',paint)
    canvas.bind('<ButtonRelease-1>',reset)

init()
screen.mainloop()