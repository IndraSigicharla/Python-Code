from itertools import accumulate
a = 97
b = 100
c = 98
n = int(input())
d1 = b - a
d2 = c - b
acc = [0, a]
acc.extend([d1, d2]*(n-2))
x = list(accumulate(acc))
print(x[n])
