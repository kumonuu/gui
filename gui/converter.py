import tkinter as tk

def convert():
    kg = float(entry.get())
    kg_gram = kg * 1000
    kg_pounds = kg * 2.205
    kg_ounce = kg * 35.274
    gramvar.set(str(kg_gram))
    poundsvar.set(str(kg_pounds))
    ouncevar.set(str(kg_ounce))

screen = tk.Tk()
screen.title("Converter")
screen.geometry("500x200")

prompt = tk.Label(screen, text="Enter the weight in Kg:")
prompt.place(x=20,y=20)

entry = tk.Entry(screen)
entry.place(x=170,y=20)
gramvar = tk.StringVar()
gram = tk.Label(screen, text="Gram")
gram.place(x=20,y=140)
grambox = tk.Label(screen, width=10, textvariable=gramvar, relief='sunken')
grambox.place(x=20,y=160)

poundsvar = tk.StringVar()
pounds = tk.Label(screen, text="Pounds")
pounds.place(x=170,y=140)
poundsbox = tk.Label(screen, width=10, textvariable=poundsvar, relief='sunken')
poundsbox.place(x=170,y=160)

ouncevar = tk.StringVar()
ounce = tk.Label(screen, text="Ounce")
ounce.place(x=320,y=140)
ouncebox = tk.Label(screen,width=10, textvariable=ouncevar, relief='sunken')
ouncebox.place(x=320,y=160)

button = tk.Button(screen, text="Convert", cursor='hand2', command=convert)
button.place(x=360,y=20)

screen.mainloop()