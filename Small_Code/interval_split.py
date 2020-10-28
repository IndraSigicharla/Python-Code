n = int(input())
a = int(input())
b = int(input())
my_list = []
c = n - a - b
if c in (a, b):
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
else:
    print("Cannot be written")
x = sorted(my_list, reverse=True)
for _ in x:
    print(_, end=" ")