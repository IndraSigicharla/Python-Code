from math import ceil
a = [int(input()) for i in range(9)]
t1 = a[0]/a[8] + a[1]/a[4] + a[2]/a[6] + a[3]/a[5]
t2 = a[3]/a[4] + a[2]/a[6] + a[1]/a[5] + a[0]/a[7]
x = ceil(t1 + t2)
print(x//60, x % 60)
