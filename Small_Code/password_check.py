import re
check1 = "^[a-zA-Z]"
check2 = "[0-9]+"
check3 = "\W"
A = 0
x = input()
a = re.search(check1, x)
b = re.search(check2, x)
c = re.findall(check3, x)
if a and b: A = 1
if (A and c) and len(x) >= 8:
    print("Valid")
else:
    print("Invalid")


# Given a word, check if it is a valid password or not.  A password is said to be valid if it satisfies the following conditions:
# *i) Should begin with a letter
# *ii) Should contain atleast one digit and one special character
# *iii) Length of the password should be atleast 8
# *Print ‘Valid' if the given word satisfies the above three conditions  and print ‘Invalid’ otherwise.