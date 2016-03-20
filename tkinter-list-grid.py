from tkinter import *

root = Tk()

mylist = [] # create the list as a global variable so all functions can access it

def add():
    global mylist
    user_item = user_entry.get()
    mylist.append(user_item)
    listbox.insert(END, user_item)
    user_entry.delete(0, 'end')
    statusText.set("Added {0} to the list".format(user_item))
    print(mylist) # testing


def remove():
    global mylist
    select = listbox.curselection() # Set a variable for the currently selected item
    print(select)
    for i in enumerate(select): #set a for loop to iterate through selected items
        index = i
        print(index)
        mylist.pop(index)   # use the same index to remove from the list
        listbox.delete(index,index) #use the index to remove the item from the listbox
        statusText.set("Removed an item from the list")
        print(mylist) # testing


def close():
    root.destroy()

       


""" Interface Elements """

#bg_image = PhotoImage(file ="backdrop.png")
root.geometry("350x215")
root.title("My List Programme")
#Base = Label(root,image = bg_image, padx=10, pady=20)
#Base.place(x=0, y=0, relwidth=1, relheight=1)

rootFrame = Frame(root, bg="#006494", padx=10, pady=10)
rootFrame.pack(fill=BOTH)

""" Create the listbox area """

listFrame = Frame(rootFrame,bg="#00486b", padx=10, pady=10)
listFrame.grid(row=0, column=0)
listbox = Listbox(listFrame, bg="#00486b", fg="#ffffff", width=12, borderwidth=0, highlightthickness=0)
listbox.grid(row=0, column=0)

# create a toolbar
btn_bg="#0090d0"
toolbar = Frame(rootFrame,bg="#006494", padx=10)
toolbar.grid(row=0, column=1, sticky=N)

""" Create the items in the toolbar frame """
# Create the Text Entry field and related button
user_entry = Entry(toolbar, width=15) # Set the entry as a variable so it can be used in the function
user_entry.grid(row=0,column=0) # Display the variable using the grid layout
btn_add = Button(toolbar, text="Add", bg=btn_bg, borderwidth=0, width=5, padx=10, pady=3, highlightthickness=0, command=add)
btn_add.grid(row=0, column=1, padx=10)

# Create the Remove Button
btn_remove = Button(toolbar, text="Remove", bg=btn_bg, borderwidth=0, width=5, padx=10, pady=3, highlightthickness=0, command=remove)
btn_remove.grid(row=1, column=1, pady=5)

# Create the Close Button
btn_close = Button(toolbar, text="Close", bg=btn_bg, borderwidth=0, width=5, padx=10, pady=3, highlightthickness=0, command=close)
btn_close.grid(row=2, column=1)


""" Create a Status Area """
statusText = StringVar()
status = Label(rootFrame, textvariable=statusText, bd=0, relief=SUNKEN, anchor=W, bg="#006494", pady=5)
status.grid(row=1, column=0, columnspan=2, sticky=W+E)



# Run the main loop
mainloop()



