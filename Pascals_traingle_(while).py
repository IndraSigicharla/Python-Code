from math import factorial as f

n = int(input("Enter a number: "))
x = -1
while x < n:
    print()
    x += 1
    if x == n:
        continue
    i = -1
    while i <= x:
        i += 1
        if i > x:
            continue


        def c(y, r):
            return f(y) // (f(r) * f(y - r))


        print(c(x, i), end=" ")
