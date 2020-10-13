def pattern():
    n = int(input("Enter a number: "))
    for i in range(0, n):
        for j in range(1, i + 2):
            print(j, end="")
        print("\r")

pattern()