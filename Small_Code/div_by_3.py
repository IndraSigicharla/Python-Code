n = int(input("Enter a number: "))
div = [x for x in range(n + 1) if x % 3 == 0]
print(" ".join([str(t) for t in div]))
