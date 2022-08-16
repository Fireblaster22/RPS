from tkinter import *
root=Tk()

def click1():
    user_input=="rock"
def click2():
    user_input=="paper"
def click3():
    user_input=="scissors"

button1 = Button(root, text="rock", command=click1)
button2 = Button(root, text="paper", command=click2)
button3 = Button(root, text="scissors", command=click3)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)

root.mainloop()

