import tkinter as tk

screen = tk.Tk()
screen.title("Address Book")
screen.geometry("500x500")

addresses = {}

def open_book():
    pass

def update_add():
    key = nameInput.get()
    addressVal = addressInput.get()
    mobileVal = mobileInput.get()
    emailVal = emailInput.get()
    bdayVal = bdayInput.get()
    addresses[key] = [addressVal,mobileVal,emailVal,bdayVal]
    listbox.insert(tk.END,key)

def edit():
    pass

def delete():
    pass

def save():
    pass

name = tk.Label(screen,text="Name:").place(x=270,y=80)
address = tk.Label(screen,text="Address:").place(x=270,y=130)
mobile = tk.Label(screen,text="Mobile:").place(x=270,y=180)
email = tk.Label(screen,text="Email:").place(x=270,y=230)
bday = tk.Label(screen,text="Birthday:").place(x=270,y=280)

nameInput = tk.Entry(screen)
nameInput.place(x=340,y=80)
addressInput = tk.Entry(screen)
addressInput.place(x=340,y=130)
mobileInput = tk.Entry(screen)
mobileInput.place(x=340,y=180)
emailInput = tk.Entry(screen)
emailInput.place(x=340,y=230)
bdayInput = tk.Entry(screen)
bdayInput.place(x=340,y=280)

openBtn = tk.Button(screen,text="Open",command=open_book).place(x=270,y=30)
updateAddBtn = tk.Button(screen,text="Update/Add",command=update_add).place(x=370,y=330)
editBtn = tk.Button(screen,text="Edit",command=edit).place(x=20,y=330)
deleteBtn = tk.Button(screen,text="Delete",command=delete).place(x=80,y=330)
saveBtn = tk.Button(screen,text="Save",width=50,command=save).place(x=60,y=380)

listbox = tk.Listbox(screen,width=30,height=15)
listbox.place(x=20,y=30)


screen.mainloop()