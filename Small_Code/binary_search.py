def binary(lst, x):
    global i
    lh = 0
    uh = len(lst) - 1
    mid = 0
    i = 0
    while lh <= uh:
        i += 1
        mid = (uh + lh) // 2
        if lst[mid] < x:
            lh = mid + 1
        elif lst[mid] > x:
            uh = mid - 1
        else:
            return mid
    return -1
n = int(input("Number of pizzas: "))
a, b, c, d = [], [], [], []
for _ in range(n):
    a.append(int(input()))
    b.append(input())
    c.append(int(input()))
    d.append(int(input()))
sortedList = sorted(list(zip(a, b, c, d)))
a, b, c, d = zip(*sortedList)
searchTerm = int(input())
_id = binary(a, searchTerm)
if _id != -1:
    print(b[_id])
    print(d[_id])
print(i)