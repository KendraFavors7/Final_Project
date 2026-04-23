# Kendra Favors
# 4/17/2026
# Final Project
# This program runs a cybersecurity game

import random
import time

# shows player stats
def show_stats(player):
    print("\n--- Player Stats ---")
    print("Energy:", player["energy"])
    print("Score:", player["score"])

# ask user what they want to do
def get_choice():
    print("\nWhat do you want to do?")
    print("1. Scan for threats")
    print("2. Rest")
    return input("Enter 1 or 2: ")

# handles what happens after a choice
def handle_choice(player, choice):
    if choice == "1":
        print("Scanning system...")
        time.sleep(1)

        event = random.randint(1, 3)
        if event == 1:
            print("You stopped a cyber attack!")
            player["score"] += 15
        elif event == 2:
                print("You found nothing.")
        else:
            print("You got tired while scanning.")
            player["energy"] -= 10

    elif choice == "2":
        print("You take a break...")
        time.sleep(1)
        player["energy"] += 10

    else:
        print("Invalid choice")

# main function
def main():
    player = {
        "energy": 50,
        "score": 0
    }

    print("Welcome to the Cybersecurity Game!")

    while player["energy"] > 0:
        show_stats(player)
        choice = get_choice()
        handle_choice(player, choice)

# small energy drain each round
    player["energy"] -= 5

    print("\nGame over! Your final score is:", player["score"])

# start the game
main()