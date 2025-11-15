import tkinter as tk

screen = tk.Tk()
screen.title("Painty")
screen.geometry("500x500")

active_btn = None
x = None
y = None

def pen():
    activate(pen_btn)

def brush():
    activate(brush_btn)

def color():
    pass

def eraser():
    activate(eraser_btn)

def reset(event):
    global x, y
    x = None
    y = None

def paint(event):
    global x, y
    if x and y:
        canvas.create_line(x,y,event.x,event.y,fill="green",smooth=True,capstyle="round")
    print(x,y,event.x,event.y)
    x = event.x
    y = event.y

def activate(btn):
    active_btn.config(relief="raised")
    btn.config(relief="sunken")
    print("button activated")

    
canvas = tk.Canvas(screen,bg="white",width=400,height=400)
canvas.grid(row=30,column=30,padx=50,pady=50)
    
pen_btn = tk.Button(screen,text="Pen",command=pen)
pen_btn.place(x=30,y=10)
brush_btn = tk.Button(screen,text="Brush",command=brush)
brush_btn.place(x=120,y=10)
color_btn = tk.Button(screen,text="Color",command=color)
color_btn.place(x=210,y=10)
eraser_btn = tk.Button(screen,text="Eraser",command=eraser)
eraser_btn.place(x=300,y=10)

def init():
    global active_btn
    active_btn = pen_btn
    canvas.bind('<B1-Motion>',paint)
    canvas.bind('<ButtonRelease-1>',reset)

init()




screen.mainloop()