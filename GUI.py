from tkinter import *

top = Tk()

top.geometry("300x200")

lbl1 = Label(top, text="List of Colours",fg="red",bg="yellow")

lbl1.place(x=10,y=10)

lb = Listbox(top,height=5)

lb.insert(1,"Red")

lb.insert(2, "Yellow")

lb.insert(3, "Green")

lb.insert(4, "Blue")

lb.place(x=10,y=30)

lbl2 = Label(top, text="List of Fruits",fg="blue",bg="green")

lbl2.place(x=160,y=10)

lb1 = Listbox(top,height=5)

lb1.insert(1,"Mango")

lb1.insert(2, "Grapes")

lb1.insert(3, "Banana")

lb1.insert(4, "Berry")

lb1.place(x=160,y=30)

top.mainloop()