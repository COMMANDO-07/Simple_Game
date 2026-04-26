# stone paper scissors game

import random  # used to generate computer choice randomly

# available choices in the game
choices = ["stone", "paper", "scissors"]

# function to play one round of game
def play_game():
    # take input from user
    user = input("Enter your choice (stone/paper/scissors): ").lower()
    
    # check if user input is valid
    if user not in choices:
        print("Invalid choice")
        return
    
    # computer randomly selects choice
    computer = random.choice(choices)
    
    print("Computer chose:", computer)
    
    # check all conditions
    if user == computer:
        print("Result: Draw")
    elif user == "stone" and computer == "scissors":
        print("Result: You win")
    elif user == "paper" and computer == "stone":
        print("Result: You win")
    elif user == "scissors" and computer == "paper":
        print("Result: You win")
    else:
        print("Result: Computer wins")

# main menu function
def game():
    while True:
        # display menu options
        print("Menu")
        print("1. Play Game")
        print("2. Exit")
        print("-"*30)
        
        # take user menu choice
        choice = input("Enter your choice: ")
        print("-"*30)
        
        # call game function
        if choice == "1":
            play_game()
        elif choice == "2":
            print("Thank you")
            break
        else:
            print("Invalid choice")

# start the game
game()