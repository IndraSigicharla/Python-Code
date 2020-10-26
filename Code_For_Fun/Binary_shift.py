v = int(input())
p = int(input())
a = bin(v)              # Converts integer to binary, and the next part slices the "0b" part off.
a = a[2:]
x = v // 2**(p - 1)     # Equivalent to right-shift of bits. (x >> y).
y = v * 2**(p - 1)      # Equivalent to left-shift of bits. (x << y).
if x & 1 == 1:
    print(x)
else:
    print(y)