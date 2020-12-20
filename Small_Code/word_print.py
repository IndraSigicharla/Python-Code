from pprint import pprint
x = input().lower().split()
print(x)
a = [i for i in x]
print(a)
bc = "1234567890!?.,:;"
a = [a[i].replace(a[i][-1], "") if a[i][-1] in bc else a[i] for i in range(len(a))]
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
pprint(d)