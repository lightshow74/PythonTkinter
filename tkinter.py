from tkinter import *

root = Tk()

bg_image = PhotoImage(file ="backdrop.png")
Base = Label(root,image = bg_image, padx=10, pady=10)
Base.place(x=0, y=0, relwidth=1, relheight=1)

def main():
    interface()


def interface():
    
   

    Label(Base, text="Name").grid(row=0, column=0)
    Entry(Base).grid(row=0, column=1)

main()
