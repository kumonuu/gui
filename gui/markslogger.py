import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import *

screen = tk.Tk()
screen.title("STUDENT INFORMATION AND MARKS LOGGER")
screen.geometry("700x400")

reports = {}

def open_file():
    global reports
    reset()

    file = askopenfile(mode='r')         
    if file:
        try:
            reports = eval(file.read())
        except Exception as e:
            messagebox.showerror("Bad file", f"Could not read file:\n{e}")
            return
        for key in reports:               
            listbox.insert(tk.END, key)

def save_file():
    file = asksaveasfile(defaultextension=".txt")
    if file:
        print(reports, file=file)
    else:
        messagebox.showwarning(
            "File Was Not Saved", "Please make sure you save your file."
        )

def update_add():
    key = name_input.get()
    rollnum = rollnum_input.get()
    science_marks = science_input.get()
    maths_marks = maths_input.get()
    percent = percent_input.get()

    reports[key] = [rollnum, science_marks, maths_marks, percent]
    listbox.insert(tk.END, key)
    clear_entries()

def edit():
    index = listbox.curselection()
    if index:
        key = listbox.get(index)
        name_input.insert(0, key)
        rollnum_input.insert(0, reports[key][0])
        science_input.insert(0, reports[key][1])
        maths_input.insert(0, reports[key][2])
        percent_input.insert(0, reports[key][3])
    else:
        messagebox.showerror(
            "No Report Selected", "You must select a report to edit it."
        )

def delete():
    index = listbox.curselection()
    if index:
        key = listbox.get(index)
        listbox.delete(index)
        del reports[key]
    else:
        messagebox.showerror(
            "No Report Selected", "You must select a report to delete it."
        )

def clear_entries():
    name_input.delete(0, tk.END)
    rollnum_input.delete(0, tk.END)
    science_input.delete(0, tk.END)
    maths_input.delete(0, tk.END)
    percent_input.delete(0, tk.END)

def reset():
    global reports          # make sure we clear the GLOBAL dict
    reports = {}
    clear_entries()
    listbox.delete(0, tk.END)

title = tk.Label(screen, text="STUDENT REPORT LOG").place(x=25, y=10)
name = tk.Label(screen, text="Name:").place(x=40, y=60)
rollnum = tk.Label(screen, text="Roll Number:").place(x=40, y=90)
science_marks = tk.Label(screen, text="Science Marks:").place(x=430, y=60)
maths_marks = tk.Label(screen, text="Maths Marks:").place(x=430, y=90)
percent = tk.Label(screen, text="Percentage:").place(x=430, y=120)

name_input = tk.Entry(screen)
name_input.place(x=130, y=60)
rollnum_input = tk.Entry(screen)
rollnum_input.place(x=130, y=90)
science_input = tk.Entry(screen)
science_input.place(x=520, y=60)
maths_input = tk.Entry(screen)
maths_input.place(x=520, y=90)
percent_input = tk.Entry(screen)
percent_input.place(x=520, y=120)

edit_btn = tk.Button(screen, text="Edit", width=10, command=edit).place(x=5, y=370)
delete_btn = tk.Button(screen, text="Delete", width=10, command=delete).place(x=140, y=370)
open_btn = tk.Button(screen, text="Open", width=10, command=open_file).place(x=280, y=370)
update_add_btn = tk.Button(screen, text="Update/Add", width=10, command=update_add).place(x=420, y=370)
save_btn = tk.Button(screen, text="Save", width=20, command=save_file).place(x=545, y=370)

listbox = tk.Listbox(screen, width=103, height=12)
listbox.place(x=40, y=160)

screen.mainloop()   