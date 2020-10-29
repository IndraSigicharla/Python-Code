import re
email = input("Enter an Email ID: ").lower()
checker = r"^\w+[\._]?[a-z0-9]+@{1}\w+[.]\w+$"
if re.search(checker,email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
print(email)
