x = int(input())
a = [input() for _ in range(x)]
b = [input() for _ in range(x)]
my_dict = {key: val for(key, val) in zip(a, b)}
for m in b:
    if int(m[-1]) % 2 == 0:
        print(m)
    else:
        print("Doesn't end with even number")
