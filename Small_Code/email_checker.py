import re
email = input("Enter an Email ID: ").lower()
checker = r"^[a-z0-9]+[\._]?[a-z0-9]+@{1}\w+[.]\w+$"
if re.search(checker,email):  
    print("Valid Email ID")  
    print(email) 
else:  
    print("Invalid Email ID")   
    print(email)
   