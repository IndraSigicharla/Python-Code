from itertools import combinations as c
pos = lambda m: ((m[1][0] - m[0][0])**2 + (m[1][1] - m[0][1])**2)**0.5
n = int(input())
a = [tuple(int(input()) for _ in range(2)) for _ in range(n)]
x = list(c(a, 2))
y = list(map(pos, x))
ID = (i for i, j in enumerate(zip(x, y)) if j[-1] == min(y))
for i in ID:
    print(*x[i], sep="\n")

"""Given 'n' points in an X-Y plane , write an algorithm and the subsequent Python code to 
determine the pair of points that are closer."""