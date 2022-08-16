from tkinter import *
from random import randint
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title  ('R P S')
root.geometry("500x600")
root.config(bg="white")


rock = ImageTk.PhotoImage(file="rock.png")
paper = ImageTk.PhotoImage(file="paper.png")
scissors = ImageTk.PhotoImage(file="scissors.png")

image_list = [rock, paper, scissors]

pick_number = randint(0,2)

image_label = Label(root, image=image_list[pick_number], bd=0)
image_label.pack(pady=20)

def spin():
    pick_number = randint(0,2)
    
    image_label.config(image=image_list[pick_number])
    
    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2
        
    #If User Picks Rock

    if user_choice_value == 0: # Rock
        if pick_number == 0:
            win_lose_label.config(text="It's A Tie! Spin Again...")
        elif pick_number == 1:#Paper
            win_lose_label.config(text="Paper Cover Rock! You Lose...")
        elif pick_number == 2: # Scissors
            win_lose_label.config(text="Rock Smashes Scissors! You Win!!!")

    #If User Picks Paper

    if user_choice_value ==1: #Paper 
        if pick_number ==1:
            win_lose_label.config(text="It's A Tie Spin Again...")
        elif pick_number == 0: #Rock
            win_lose_label.config(text="Paper Cover Rock! You Win!!!")
        elif pick_number ==2: #Scissors
            win_lose_label.config(text="Scissors Cuts Paper! You Lose...")

    #If User Picks Scissors 
    
    if user_choice_value ==2: #Scissors
        if pick_number ==2:
            win_lose_label.config(text="It's A Tiel Spin Again...")
        elif pick_number == 0: #Rock
            win_lose_label.config(text="Rock Smashes Scissors! You Lose...")
        elif pick_number ==1: #Paper
            win_lose_label.config(text="Scissors Cuts Paper! You Win!!!")
    
    
user_choice= ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady=10)

win_lose_label = Label(root, text=" ", font= ("Helvetica", 10), bg= "white")
win_lose_label.pack(pady=50)

root.mainloop()