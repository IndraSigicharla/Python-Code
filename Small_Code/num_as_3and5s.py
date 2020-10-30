n = int(input())
i = 0
if n < 8:
    print("Invalid input")
elif n % 3 == 0:
    print("Only three's")
elif n % 5 == 0:
    print("Only five's")
else:
    while n % 3 != 0:
        n -= 5
        i += 1
        x = n // 3
    print(f"{x} three's and {i} five's")
