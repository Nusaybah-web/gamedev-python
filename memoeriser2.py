"""from tkinter import *
from tkinter.filedialog import *

root=Tk()"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Address Book")
root.geometry("520x380")
root.resizable(False, False)



my_adress_book={}

def clear():
    entry_name.delete(0,END)
    entry_address.delete(0,END)
    entry_mobile.delete(0,END)
    entry_email.delete(0,END)
    entry_birthday.delete(0,END)

def update():
    key=entry_name.get()
    if key=="":
        messagebox.showerror("incorrect input", "the name cannot be empty, please change it")
    else:
        if key not in my_adress_book.keys():
            lb.insert(END,key)
        my_adress_book[key]=(entry_address.get(),entry_mobile.get(),entry_email.get(),entry_birthday.get())
        clear()




frame1 = Frame(root, padx=10, pady=10)
frame1.grid(row=0, column=0, sticky="n")

la = Label(frame1, text="My Address Book")
la.grid(row=0, column=0, columnspan=2)

lb = Listbox(frame1, width=30, height=14)
lb.grid(row=1, column=0, columnspan=2, pady=5)

edit=Button(frame1, text="Edit", width=10)
edit.grid(row=2, column=0, pady=10)

delete = Button(frame1, text="Delete", width=10)
delete.grid(row=2, column=1, pady=10)


frame2 = Frame(root, padx=10, pady=10)
frame2.grid(row=0, column=1, sticky="n")

button_open = Button(frame2, text="Open", width=10)
button_open.grid(row=0, column=1, sticky="e", pady=(0, 10))

label_name = Label(frame2, text="Name:")
label_name.grid(row=1, column=0, sticky="w")
entry_name = Entry(frame2, width=25)
entry_name.grid(row=1, column=1, pady=5)

label_address = Label(frame2, text="Address:")
label_address.grid(row=2, column=0, sticky="w")
entry_address = Entry(frame2, width=25)
entry_address.grid(row=2, column=1, pady=5)

label_mobile = Label(frame2, text="Mobile:")
label_mobile.grid(row=3, column=0, sticky="w")
entry_mobile = Entry(frame2, width=25)
entry_mobile.grid(row=3, column=1, pady=5)

label_email = Label(frame2, text="Email:")
label_email.grid(row=4, column=0, sticky="w")
entry_email = Entry(frame2, width=25)
entry_email.grid(row=4, column=1, pady=5)

label_birthday = Label(frame2, text="Birthday:")
label_birthday.grid(row=5, column=0, sticky="w")
entry_birthday = Entry(frame2, width=25)
entry_birthday.grid(row=5, column=1, pady=5)

button_update = Button(frame2, text="Update/Add", width=15,command=update)
button_update.grid(row=6, column=1, pady=10)

button_save = Button(root, text="Save", width=30)
button_save.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()

