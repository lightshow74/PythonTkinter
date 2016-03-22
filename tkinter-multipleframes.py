from tkinter import *


def raise_frame(frame):
    frame.tkraise()

root = Tk()

root.geometry("350x350")
root.configure(bg="#ffcc00")

f1 = Frame(root, bg="#ffcc00")
f2 = Frame(root, bg="#ffcc00")
f3 = Frame(root, bg="#ffcc00")
f4 = Frame(root, bg="#ffcc00")

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Label(f1, text='FRAME 1').pack(fill=BOTH)

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()
