x = int(input())
a, b = [], []
for _ in range(x):
    a.append(input())
    b.append(int(input()))
my_dict = {key: val for (key, val) in zip(a, b)}
for m, n in my_dict.items():
    print(m)
    print(n)
print(sum(b))
my_dict.pop(a[0])
my_dict.pop(a[-1])
for v, w in my_dict.items():
    print(v)
    print(w)
