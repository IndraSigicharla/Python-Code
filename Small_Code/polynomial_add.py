d1 = int(input())
a = [int(input()) for i in range(d1 + 1)]
d2 = int(input())
b = [int(input()) for i in range(d2 + 1)]
m = a[::-1]
n = b[::-1]
m.extend([0] * (d2 - d1))
x = m[::-1]
n.extend([0] * (d1 - d2))
y = n[::-1]
result = [sum(list(i)) for i in list(zip(x, y))]
print(result)

# *Write an algorithm and the subsequent Python program to add the two given polynomials.
# *Assume that the coefficients of each polynomial are stored in a separate list.