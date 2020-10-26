n1 = input()[::-1]
n2 = input()[::-1]
y = 1
for i, idx in enumerate(n1):
    if idx == n2[i]:
        if i == 0:
            print("Same at 1's position")
            y = 0
        elif i in range(1, len(n1) + 1):
            print(f"Same at {10**i}th position")
            y = 0
if n1[i] != n2[i] and y:
    print("No digits are same")