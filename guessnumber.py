#Guess Number
#Store the random number and guessing number in Variable
#Conditions ---> Checks if the guess is too high, too low, or correct
#Loop--> Allow multiple guesses until the correct is found
import random

random_number =random.randrange(1,50)

print("Start Playing Guessing Number Game")
guessed_number=int(input("Please enter number between 1 and 50:-"))

trials=1
while trials<=5:
    if random_number == guessed_number:
        print("Superb! You got it.")
        break
    elif random_number<guessed_number:
        print("Your guessed number is high.")
    elif random_number>guessed_number:
        print("Your guessed number is low.")
    trials+=1
    if(trials<=5):
        print("Please Try Once Again")
        guessed_number = int(input("Please enter number between 1 and 50:-"))
    else:
        print("You have tried 5 times.Better luck next time.")



