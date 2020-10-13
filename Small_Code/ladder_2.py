def pattern():
    n = int(input("Enter a number: "))
    for i in range(0, n + 1 , 2):
        for j in range(2, i + 2, 2):
            print(j, end="")
        print("\r")

pattern()
