import random
randNumber = random.randint(1, 100)
# print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("you guessed it right!")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong! enter the smaller number")
        else:
            print("you guessed it wrong! enter the larger number")
    
print(f"you guessed the number in {guesses} gusesses")