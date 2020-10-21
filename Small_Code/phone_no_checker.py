n = input("Enter a phone number: ")
if len(n) != 10 and n[0] == "0":
    print("Invalid Number")
    exit()
else:
    print("Valid Number")