a = int(input("Enter the year: "))
b = "The year {} is a leap year."
if a % 4 == 0:
    print(b.format(a))
else:
    print("This year is not a leap year.")
