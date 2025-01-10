#Evan Chen
#1/6/2024
import random
wins = 0
losses = 0
ties = 0

def rpsgame():
    global wins
    global losses
    global ties
    print("Select rock, paper or scissors, or end")
    while True:
        user_action = input("Enter your choice: ")
        computer_action = random.randint(1, 3)
        if computer_action == 1:
            computer_action = "rock"
            print("Computer chose rock")
        elif computer_action == 2:
            computer_action = "paper"
            print("Computer chose paper")
        else:
            computer_action = "scissors"
            print("Computer choose paper")

        if user_action == computer_action:
            ties == ties + 1
            print("Both players picked the same!" + 'ties')

        elif user_action == "rock":
            if computer_action == "scissors":
                wins == wins + 1
                print("Rock crushes scissors! You win!" + 'wins')
            else:
                losses == losses + 1
                print("Paper wraps the rock! You lose!" + 'losses')
        elif user_action == "paper":
            wins == wins + 1
            if computer_action == "rock":
                print("You wrapped the rock! You win!" + 'wins')
            else:
                losses == losses + 1
                print("Oh no! You were cut up! You lose!" + 'losses')
        elif user_action == "scissors":
            if computer_action == "paper":
                wins == wins + 1
                print("Cut the paper!!! You win!" + 'wins')
            else:
                losses == losses + 1
                print("You were crushed by the rock. You lose!" + 'losses')
        elif user_action == "end":
                print("The game has ended")
                break


rpsgame()


