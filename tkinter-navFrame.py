from tkinter import *

""" Functions """

def raise_frame(frame):
    frame.tkraise()


""" Graphical Interface """

root = Tk()

root.title("Multiple Frames")
#root.geometry("350x350")
root.configure(bg="#006494")

# Base frame to wrap all elements and act as a common background #
rootFrame = Frame(root, bg="#006494", padx=5, pady=5)
rootFrame.grid(row=0, column=0)
rootFrame.grid_rowconfigure(0, minsize=250)
rootFrame.grid_columnconfigure(0, weight=1, minsize=250)

navFrame = Frame(root, padx=10, pady=10, bg="#ffcc00")
navFrame.grid(row=1, column=0)
navFrame.grid_rowconfigure(1, weight=1)
navFrame.grid_columnconfigure(0, minsize=250)

# Frame Definition #
f1 = Frame(rootFrame, bg="#006494")
f2 = Frame(rootFrame, bg="#006494")
f3 = Frame(rootFrame, bg="#006494")
f4 = Frame(rootFrame, bg="#006494")

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky="NEWS")
    frame.grid_columnconfigure(0, weight=1, minsize=250)
    

# Frame 1 Content #
f1_h1 = Label(f1, text='Frame 1', font=("Helvetica", 16), bg="#BB6494", fg="#FFFFFF", anchor=CENTER)
f1_h1.grid(row=0, column=0)

f1_h2 = Label(f1, text="Hello World", anchor=W)
f1_h2.grid(row=1, column=0)


# Frame 2 Content #
Label(f2, text='Frame 2').pack(fill=BOTH)
    
# Navigation #
btn1 = Button(navFrame, text='One', command=lambda:raise_frame(f1))
btn1.grid(row=0, column=0)

btn2 = Button(navFrame, text='Two', command=lambda:raise_frame(f2))
btn2.grid(row=0, column=1)

btn3 = Button(navFrame, text='Three', command=lambda:raise_frame(f3))
btn3.grid(row=0, column=2)

raise_frame(f1)
root.mainloop()
