import os
import time
import random
from threading import Timer

whutlmao = int(input("Timer limit: "))


def exitfunc():
    os._exit(0)


Timer(whutlmao, exitfunc).start()


class Guess:
    def __init__(self, guess, rand_no, guess_count, x):
        self.guess = guess
        self.random = rand_no
        self.guess_count = guess_count
        self.x = x

    def determine(self):

        while self.guess is not self.random:
            while True:
                if 0 <= self.guess <= 100:
                    break
                else:
                    print("Invalid! Try again!")
                    self.guess = int(input("Enter a random number between 1 and 100:\n"))
            if self.random > self.guess:
                print("Guess a Higher number please")
            else:
                print("Guess a Lower number please")
            self.guess_count += 1
            self.guess = int(input("Enter a random number between 1 and 100:\n"))
            if self.guess_count == 5 and self.guess is not self.random:
                self.x = False
                break
            elif self.guess_count == 5:
                break

        if self.x:
            print("Congratulations,You have won!You guessed the right number {} in {} tries".format(self.random,
                                                                                                    self.guess_count))
        else:
            print("You have lost! You were given {} chances and you couldn't guess the right number {}!".format(
                self.guess_count, self.random))


randNo = random.randint(0, 100)
guess = int(input("Enter a random number between 1 and 100:\n"))
GuessCount = 1
x = True
Gue = Guess(guess, randNo, GuessCount, x)
Gue.determine()
time.sleep(1)