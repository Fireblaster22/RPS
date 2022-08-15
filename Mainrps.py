import random
from tkinter import *
root=Tk()


user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

def click1():
    user_input=="rock"
def click2():
    user_input=="paper"
def click3():
    user_input=="scissors"

button1 = Button(root, text="rock", command=click1)
button2 = Button(root, text="paper", command=click2)
button3 = Button(root, text="scissors", command=click3)



while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("Its a Draw!")

    elif user_input == "paper" and computer_pick == "paper":
        print("Its a Draw!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Its a Draw!")
        user_wins += 1


    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)

root.mainloop()
