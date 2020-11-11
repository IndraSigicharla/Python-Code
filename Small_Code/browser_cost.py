h = int(input("Enter the numbers of hours used: "))
m = float(input("Enter the number of minutes used: "))
amt = 0
if h >= 7 and m > 0:
    exit("Invalid Entry")
elif h >= 5:
    amt += 200 + (h-5) + m
else:
    amt = h*50 + m
print(f"The cost of browsing the web is: {amt}")
