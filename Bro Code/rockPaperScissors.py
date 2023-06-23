import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors: ").lower()

    if computer == player:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")

    elif computer == "rock":
        if player == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")
        elif player == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")

    elif player == "rock":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")
        elif computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")

    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")

    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")
        elif computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")

    option = input("Do you want to play again: (yes)/(no)?: ").lower
    if option != "yes":
        break