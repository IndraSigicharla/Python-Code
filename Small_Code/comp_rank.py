x = [input().split(" ", 1)[::-1] for i in range(int(input()))]
a = sum(x, [])
umm = a[::]
del a[1::2]
del umm[0::2]
b = list(map(int, " ".join(a).split()))
for _ in range(0, len(b), 3):
    b[_] *= 10
for _ in range(1, len(b), 3):
    b[_] *= 30
for _ in range(2, len(b), 3):
    b[_] *= 50
b = [b[i:i + 3] for i in range(0, len(b), 3)]
c = list(map(sum, b))
d = sorted(c, reverse=True)
d = [1 if x == max(d) else x for x in d]
for _ in range(10000):
    d = [len(d[:d.index(max(d))]) + 1 if x == max(d) else x for x in d]
muu = [u for _, u in sorted(zip(c, umm), key=lambda sl: (-sl[0], sl[1]))]
for i, j in zip(d, muu):
    print(str(i) + "   " + str(j))

# Sample Input:
# 6
# Student1 12 8 9
# Student2 11 8 11
# Student3 10 7 10
# Student4 13 7 8
# Student5 12 8 9
# Student6 21 6 7
