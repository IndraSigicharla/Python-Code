n = float(input("Enter the amount of money in hand: "))
c = float(input("Enter the cost of one chocolate: "))
m = int(input("Enter the number of wrappers for a free chocolate: "))
p = n//c
f = p//m
print("Number of chocolates are",int(p+f))
