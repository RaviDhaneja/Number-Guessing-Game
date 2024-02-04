import random

user_input=input("Enter a Choice(rock,paper,scissors) :")
user_text = user_input.lower()
possible=["rock","paper","scissors"]
computer_choice = random.choice(possible)
print("your choice: "+ user_text + " computer choice: "+computer_choice)
if user_text == computer_choice or user_text == computer_choice:
    print("Both players selected"+user_text+"It's a tie!")
elif user_text == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_text == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_text == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")