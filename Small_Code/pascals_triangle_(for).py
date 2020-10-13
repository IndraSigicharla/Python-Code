from math import factorial as f

n = int(input("Enter a number: "))
for x in range(0, n):
    print()
    for i in range(0, x + 1):
        def c(y, r):
            return f(y) // (f(r) * f(y - r))
        print(c(x, i), end=" ")
