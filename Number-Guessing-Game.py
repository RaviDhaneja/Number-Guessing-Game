import random

RandomNumber=random.randint(1,100)
YourNumber=0
count=0
while YourNumber != RandomNumber:
    YourNumber=int(input("Enter a number between 1 and 100 :- "))
    count+=1
    if (YourNumber < RandomNumber):
        print(" Too Low !")     
    elif (YourNumber>RandomNumber):
        print("Too high !")
    elif(YourNumber == RandomNumber):
        print("You Guessed it !")
        print("Number of Guesses:- " + str(count))