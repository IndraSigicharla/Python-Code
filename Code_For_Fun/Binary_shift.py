v = int(input())
p = int(input())
a = bin(v)
a = a[2:]
x = v // 2**(p - 1)
y = v * 2**(p - 1)
if x & 1 == 1:
    print(x)
else:
    print(y)