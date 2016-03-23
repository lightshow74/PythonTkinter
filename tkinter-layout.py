from tkinter import *

master = Tk()

master.geometry("300x300")

inputfields = LabelFrame(master, text="Input Fields", padx=5, pady=5)
inputfields.grid(row=0,column=0)

Label(inputfields, text="First", width=10, anchor=E).grid(row=0,column=0)
Label(inputfields, text="Second", width=10, anchor=E).grid(row=1,column=0)
Label(inputfields, text="Options", width=10, anchor=E).grid(row=2,column=0)

Entry(inputfields).grid(row=0, column=1)
Entry(inputfields).grid(row=1, column=1)

Checkbutton(inputfields).grid(row=0,column=2, sticky=W)
Checkbutton(inputfields).grid(row=1,column=2, sticky=W)

variable = StringVar(inputfields)
variable.set("one") # default value
OptionMenu(inputfields, variable, "one", "two", "three").grid(row=2,column=1,sticky=W)


submits = LabelFrame(master, text="Submit Fields", padx=5, pady=5)
submits.grid(row=1,column=0)

Button(submits, text="Send").grid(row=1,column=1)


mainloop()