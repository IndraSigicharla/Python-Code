"""Pocket money increases weekly to purchase a game,
output is the no. of weeks to get the game."""

from itertools import accumulate

x = int(input())                    # Cost of the game, sample input = 100
p = int(input())                    # Initial pocket money, sample input = 20
q = int(input())                    # Increment per week, sample input = 2

# First way to write the code:
a = [p, *[q]*(50)]
b = list(accumulate(accumulate(a)))
for m, n in enumerate(b):
    if n > x:
        print(m + 1)
        break

# Second way to write the code:

pm = 0
i = 0
while pm <= x:
    pm = pm + p + i*q
    i += 1
print(i)
