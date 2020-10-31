from itertools import combinations
x = int(input())
y = input().split()
z = int(input())
a = list(combinations(range(1, x + 1), z))
b = [m + 1 for m, n in enumerate(y) if n == "a"]
print(float(len({w for v in b for w in a if v in w})) / len(a))
