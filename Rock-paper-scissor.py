import random

user=input("Enter a Choice(rock,paper,scissors) :")
possible=["rock","paper","scissors"]
computer_choice = random.choice(possible)
print("your choice: "+ user + " computer choice: "+computer_choice)
if user == computer_choice:
    print("Both players selected"+user+"It's a tie!")
elif user == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")