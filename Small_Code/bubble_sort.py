def sorter(lst):
    for x in range(len(lst)):
        for y in range(len(lst)-x-1):
            if lst[y] > lst[y+1]:
                lst[y], lst[y+1] = lst[y+1], lst[y]
    return lst
number = int(input())
a, b, c, d = [], [], [], []
for _ in range(number):
    a.append(int(input()))
    b.append(input())
    c.append(int(input()))
    d.append(int(input()))
e = d[::]
sorter(d)
for i, j in enumerate(sorter(d)):
    print(b[e.index(j)])
# 3
# 1234
# marg
# 10
# 100
# 5678
# cheese
# 20
# 50
# 9876
# pizz
# 30
# 150
