from itertools import accumulate
a = int(input())
b = int(input())
c = int(input())
n = int(input())
d1 = b - a
d2 = c - b
# *!(arg) is a change here
acc = [0, a, *[d1, d2]*(n-2)]
x = list(accumulate(acc))
print(x[n])
