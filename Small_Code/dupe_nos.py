# Code to remove consecutive duplicate numbers from input:

a = []
for x in range(int(input())):
    a.append(int(input()))
for i, x in enumerate(a):
    if a[i - 1] == a[i]:
        a.pop(i)
    if a[0] == a[1]:
        a.pop(0)
for x in a:
    print(x)
