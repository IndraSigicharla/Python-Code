a = [int(input()) for _ in range(10)]
def sorter(lst):
    for i in range(len(lst)):
        mn = i
        for j in range(i+1, len(a)):
            if lst[mn] > lst[j]:
                mn = j
        lst[i], lst[mn] = lst[mn], lst[i]
sorter(a)
print(a)