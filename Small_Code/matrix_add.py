m1, m2 = [], []
for _ in range(3):
    a = [int(input()) for _ in range(3)]
    m1.append(a)

for _ in range(3):
    b = [int(input()) for _ in range(3)]
    m2.append(b)

add = [[m1[i][j] + m2[i][j]
        for j, _ in enumerate(m1[0])] for i, _ in enumerate(m2)]

for x in add:
    for _ in x:
        print(_)
