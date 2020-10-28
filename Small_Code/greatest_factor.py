x = int(input())
y = int(input())
a = [i for i in range(1, x) if x % i == 0]
b = [i for i in range(1, y) if y % i == 0]
if max(a) == max(b):
    print(max(a))
else:
    print("No")
