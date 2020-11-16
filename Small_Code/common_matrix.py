a = int(input())
b = int(input())
c = sum((input().split() for _ in range(a)), [])
d = int(input())
e = int(input())
f = sum((input().split() for _ in range(d)), [])
for x in c:
    if x in f:
        c[c.index(x)] = "0"
c = [c[i:i + a] for i in range(0, len(c), a)]
for x in c:
    print(*x, "")

# If M3 = M1~M2 then M3[i,j] = M1[i,j] if M1[i,j] ∉ M2 and M3[i,j] = 0 otherwise where M1[i,j] ∉ M2 indicates that M1[i,j] is not an element of matrix M2. Given two matrices M1 and M2 write a code to find M1~M2.
