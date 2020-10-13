print("The general form of a quadratic equation is ax^2 + bx + c = 0")
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))
c = float(input("Enter the value of 'c': "))
root1 = (-b + ((b**2) - 4*a*c) ** 0.5) / 2*a
root2 = (-b - ((b**2) - 4*a*c) ** 0.5) / 2*a
if (b**2) - 4*a*c >= 0:
    print("The roots are real.")
    print(format(root1,".2f"),format(root2, ".2f"))
else:
    print("The roots are not real.")
    print(format(root1,".2f"),format(root2, ".2f"))
