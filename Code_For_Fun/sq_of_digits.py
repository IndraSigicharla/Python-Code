n = input()
i = 0
while int(n) > 4 and i < 10:
    n = str(sum(int(x)**2 for x in n))
    i += 1
if int(n) == 4:
    print(i)
else:
    print("No")
