import random

# randomRange = random.randrange(-3, 11)
# randomInt =  random.randint(0, 10)
# print(randomRange)
# print (randomInt)
print("Hello There! Welcome to Guess a number game!")
play = input("Do you want to play?(yes/no): ")
if play.lower() == 'yes':
    print("Okay, Let's play, Have fun!")
else:
    print("Okay, Byee!")
    quit()

bigNumber = input("Enter the highest number you would like to guess: ")
if bigNumber.isdigit():
    bigNumber = int(bigNumber)
    if bigNumber <= 0 :
        print("Enter a number greater than 0")
        quit()
else :
    print("Enter a digit number next time")
    quit()

randomNumber = random.randint(0, bigNumber)

totalGuesses = 0
while True:
    totalGuesses += 1
    randomGuess= input("Make a random Number guess: ")
    if randomGuess.isdigit():
        randomGuess = int(randomGuess)
    else :
        print("Enter a digit number next time")
        continue
    if randomGuess == randomNumber :
        print("correct")
        print("You got it correct in", totalGuesses, "guesses")
        break
    elif randomGuess > randomNumber :
        print("Incorrect!")
        print("You are above the Guess. Guess a lower number!")
    else:
        print("Incorrect!")
        print("You are below the correct Guess. Guess a higher number")
    continue


    

