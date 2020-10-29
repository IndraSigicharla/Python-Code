# Code to remove consecutive duplicate numbers from input:
# List-comprehension for taking user inputs and creating a list:

a = [int(input()) for _ in range(int(input()))]
for i, x in enumerate(a):
    if a[i - 1] == a[i]:
        a.pop(i)
    if a[0] == a[1]:
        a.pop(0)
for x in a:
    print(x)
