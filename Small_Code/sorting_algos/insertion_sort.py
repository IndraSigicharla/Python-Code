def sorter(lst):
    for x in range(1, len(lst)):
        Id = lst[x]
        y = x - 1
        while y >= 0 and Id < lst[y]:
            lst[y + 1] = lst[y]
            y -= 1
        lst[y + 1] = Id
    return lst


number = int(input())
a, b, c, d = [], [], [], []
for _ in range(number):
    a.append(int(input()))
    b.append(input())
    c.append(int(input()))
    d.append(int(input()))
e = [x for _, x in sorter(list(zip(d, b)))]
print(*e, sep="\n")
