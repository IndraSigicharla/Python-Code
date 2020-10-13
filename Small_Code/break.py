s = 0
while True:
    m = int(input("Enter a number: "))
    s += m
    if m % 5 == 0:
        print("You've broken out of the loop!")
        print("Sum =", s)
        print("The number which broke you out of the loop is", m)
        break
    else: continue
