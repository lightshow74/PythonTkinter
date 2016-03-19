from tkinter import *

root = Tk()

mylist = [] # create the list as a global variable so all functions can access it

def add():
    global mylist
    user_item = user_entry.get()
    mylist.append(user_item)
    listbox.insert(END, user_item)
    user_entry.delete(0, 'end')
    
    print(mylist) # testing


def remove():
    global mylist
    select = listbox.curselection() # Set a variable for the currently selected item

    for i in select: #set a for loop to iterate through selected items
        index = int(i)  #convert the item to an integer to get the index
        listbox.delete(index,index) #use the index to remove the item from the listbox
        mylist.pop(index)   # use the same index to remove from the list
        print(mylist) # testing


def close():
    root.destroy()

       


""" Interface Elements """

bg_image = PhotoImage(file ="backdrop.png")
root.geometry("300x200")
Base = Label(root,image = bg_image, padx=10, pady=10)
Base.place(x=0, y=0, relwidth=1, relheight=1)


# create a toolbar
btn_bg="#0090d0"
toolbar = Frame(root,bg="#00486b")

# Create the buttons
b = Button(toolbar, text="Add", bg=btn_bg, borderwidth=0, padx=10, pady=3, highlightthickness=0, command=add)
b.pack(side=LEFT, padx=10, pady=3)
b = Button(toolbar, text="Remove", bg=btn_bg, borderwidth=0, padx=10, pady=3, highlightthickness=0, command=remove)
b.pack(side=LEFT, padx=10, pady=3)
b = Button(toolbar, text="Close", bg=btn_bg, borderwidth=0, padx=10, pady=3, highlightthickness=0, command=close)
b.pack(side=LEFT, padx=10, pady=3)
toolbar.pack(side=TOP, fill=X)

# Create the Text Entry field
input_frame = Frame(root,bg="#006494")
input_frame.pack(side=TOP, fill=X) # Set a frame using the Pack layout - grid layouts can go inside this

Label(input_frame, text="Add an Item").grid(row=0,column=0) # set a label for the input using the grid layout
user_entry = Entry(input_frame) # Set the entry as a variable so it can be used in the function
user_entry.grid(row=0,column=1) # Display the variable using the grid layout

listbox = Listbox(root, width=10, borderwidth=0)
listbox.pack(side=LEFT, padx=20)


# Run the main loop
mainloop()



