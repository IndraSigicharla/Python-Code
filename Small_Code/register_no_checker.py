n = input("Enter a register number: ")
x = n[:2]
y = n[2:5]
z = n[5:]
if len(x) == 2 and len(y) == 3 and len(z) == 4:
    print("Valid Input")
else:
    print("Invalid Input")