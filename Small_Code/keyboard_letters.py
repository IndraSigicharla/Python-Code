x = input().lower()
r1 = "qwertyuiop"
r2 = "asdfghjkl"
r3 = "zxcvbnm"
i = sum(i in r1 for i in x)
j = sum(i in r2 for i in x)
k = sum(i in r3 for i in x)
if len(x) in (i, j, k):
    print("Yes")
else:
    print("No")

# *Given an  English word,  write an algorithm and the subsequent Python code to check if the given word can be typed using just a single row of the keyboard.
# *(e.g. POTTER, EQUITY). Print 'Yes' if the letters of the word are from a single row and print 'No' otherwise.