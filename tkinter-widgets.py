# Reference: http://effbot.org/tkinterbook/tkinter-index.htm

from tkinter import *

master = Tk()

def callback():
    print(e.get())
    v.set(e.get()) # uses the entered string to change the Var in w2
    
# Creates a text entry box for strings
e = Entry(master)
e.pack()
e.focus_set()   # sets the focus

# Button
b = Button(master, text="OK", command=callback)
b.pack()

# Label
w = Label(master, text="Your input was:", font=("Helvetica", 16))
w.pack()

# Changing a label to use a variable or input from text field
v = StringVar()
w2 = Label(master, textvariable=v)
w2.pack()

# Check list
var = IntVar()
c = Checkbutton(master, text="Expand", variable=var)
c.pack()

# Radio list 
v = IntVar()
Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)


# Radio list using a list and for loop
def radio_call():
    print(v.get())

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for position,day in enumerate(options):
    b = Radiobutton(master, text=day,variable=v, value=position, command=radio_call)
    b.pack(anchor=W)
    

# List Box
listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)
    
    
''' Menu Bar '''
def hello():
    print("hello!")

# create a toplevel menu
menubar = Menu(master)
menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!", command=master.destroy)

# Menu with a sub menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master.destroy)
menubar.add_cascade(label="File", menu=filemenu)

# display the menu
master.config(menu=menubar)


# Option Menu

variable = StringVar(master)
variable.set("one") # default value

o = OptionMenu(master, variable, "one", "two", "three")
o.pack()


# Status Bar

status = Label(master, text="Status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


mainloop()