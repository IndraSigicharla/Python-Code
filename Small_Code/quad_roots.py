print("The general form of a quadratic equation is ax^2 + bx + c = 0")
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))
c = float(input("Enter the value of 'c': "))
r1 = (-b + ((b**2) - 4*a*c) ** 0.5) / 2*a
r2 = (-b - ((b**2) - 4*a*c) ** 0.5) / 2*a
if (b**2) - 4*a*c >= 0:
    print("The roots are real.")
else:
    print("The roots are not real.")

print(f"{r1:.2f}, {r2:.2f}")
