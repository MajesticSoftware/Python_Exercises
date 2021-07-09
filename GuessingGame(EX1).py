##Created by Jeffrey Scruggs
import random
def geussinggame():
    randint = random.randint(0,100)
    user = input("Guess a number between 0 and 100\n")
    while user != randint:
        if user < randint:
            print("Too low")
            user = input("Guess a number between 0 and 100\n")
        elif user > randint:
            print("Too high")
            user = input("Guess a number between 0 and 100\n")
        else:
            print("Invalid response...")
            user = input("Guess a number between 0 and 100\n")

    print("Just Right")
    print("Terminating Program...")

geussinggame()