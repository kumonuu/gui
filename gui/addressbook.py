import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import *

screen = tk.Tk()
screen.title("Address Book")
screen.geometry("500x500")

addresses = {}

def open_book():
    global addresses
    reset()
    file = askopenfile()
    if file:
        addresses = eval(file.read())
        keys = addresses.keys()
        for key in keys:
            listbox.insert(tk.END,key)

def update_add():
    key = nameInput.get()
    addressVal = addressInput.get()
    mobileVal = mobileInput.get()
    emailVal = emailInput.get()
    bdayVal = bdayInput.get()
    addresses[key] = [addressVal,mobileVal,emailVal,bdayVal]
    listbox.insert(tk.END,key)
    clear_entries()

def edit():
    index = listbox.curselection()
    if index:
        item = listbox.get(index)
        nameInput.insert(0,item)
        addressInput.insert(0,addresses[item][0])
        mobileInput.insert(0,addresses[item][1])
        emailInput.insert(0,addresses[item][2])
        bdayInput.insert(0,addresses[item][3])
    else:
        messagebox.showerror("No Address Selected","You must select an address to edit it.")

def delete():
    index = listbox.curselection()
    if index:
        item = listbox.get(index)
        listbox.delete(index)
        del addresses[item] 
    else:
        messagebox.showerror("No Address Selected","You must select an address to delete it.")
        

def save():
    file = asksaveasfile(defaultextension='.txt')
    if file:
        print(addresses,file=file)
    else:
        messagebox.showwarning("File was not saved","Please make sure that the file exists.")


def clear_entries():
    nameInput.delete(0,tk.END)
    addressInput.delete(0,tk.END)
    mobileInput.delete(0,tk.END)
    emailInput.delete(0,tk.END)
    bdayInput.delete(0,tk.END)

#reset function clears entries, deletes dicts
def reset():
    addresses = {}
    clear_entries()
    listbox.delete(0,tk.END)
    
def display(event):
    screen2 = tk.Tk()
    screen2.title("Display")
    index = listbox.curselection()
    if index:
        item = listbox.get(index)
        print(addresses)
        addressVal = addresses[item][0]
        mobileVal = addresses[item][1]
        emailVal = addresses[item][2]
        bdayVal = addresses[item][3]
        info = tk.Label(screen2,text=f"{item}\nAddress: {addressVal}\nMobile: {mobileVal}\nEmail: {emailVal}\nBirthday: {bdayVal}")
        info.place(x=70,y=50)

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

listbox = tk.Listbox(screen,width=39,height=18)
listbox.place(x=20,y=30)
listbox.bind('<<ListboxSelect>>',display)

screen.mainloop()