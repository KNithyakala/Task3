#Word Scramble
#Make List with Words
#Scramble the words using String Manipulations
#Conditions --> To check the player's guess matches original word
#Loop --> Allow multiple attempt

import random
word= ['python','javascript','java','automation','pytest','guvi','selenium']
word1=random.choice(word) # random choice of word from list
word2=list(word1) # making list of characters with random choice
random.shuffle(word2) # shuffle the list of characters
word3=''.join(word2) # join the shuffled characters as one word
attempt=1
print("Lets Play Scrambled Word")
print(f"Unscramble the word:{word3}")
guessword=str(input("Enter your guessing word:")) #getting input from user
while attempt<=5: # giving 5 chance
    if guessword==word1: #check guessing word matches with random choice
        print(f"Wonderful. You got it in {attempt} time")
        break
    elif attempt<5:
        attempt+=1
        guessword=str(input("Enter your guessing word:"))
    else:
        print("Better luck next time")

