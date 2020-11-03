import random
import os
from threading import Timer
import logging
logging.basicConfig(filename="answers.log", level=logging.DEBUG)


def oof():
    if gc == 1:
        print(f"You have {gc} guess for this round.")
    else:
        print(f"You have {gc} guesses for this round.")


def clear():
    os.system("cls")


def byeguess():
    global x
    print(f"\nOoops! You ran out of time!!.\nThe correct answer was {x}.")
    os._exit(0)


clear()
diff = int(input("Enter a number for difficulty:\n1) Easy\n2) Normal\n3) Hard\n4) Random\n5) Custom\n"))
if diff == 1:
    gc = 100
elif diff == 2:
    gc = 5
elif diff == 3:
    gc = 3
elif diff == 4:
    gc = random.randint(0, 100)
elif diff == 5:
    gc = int(input("Enter the number of chances you want: "))

oof()
time = int(input("Enter timer limit (in seconds): "))
clear()
oof()

Timer(time, byeguess).start()

x = random.randint(0, 100)
logging.debug(x)
guess = 0
while True:
    num = input("Please guess a random number between 0 - 100: ")
    try:
        num = int(num)
    except ValueError:
        print("Invalid number, please guess again.")
        continue
    guess += 1
    if guess != gc:
        if num < x:
            print("Your guess was under.")
        elif num > x:
            print("Your guess was over.")
        else:
            if guess != 1:
                print(f"You guessed it in {guess} guesses!!")
            else:
                print("You guessed it on the first try!!")
            os._exit(0)
    else:
        if num == x:
            if guess != 1:
                print(f"You guessed it in {guess} guesses!!")
            else:
                print("You guessed it on the first try!!")
        else:
            print("Ooops! You ran out of guesses!!")
            print(f"The correct answer was {x}.")
        os._exit(0)
