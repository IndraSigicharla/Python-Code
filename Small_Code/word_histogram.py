from pprint import pprint
import re
x = input().lower()
check = re.search("^[a-z]*$", x)
if check:
    d = {}
    for i in x:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    inv_d = {}
    for k, v in sorted(d.items()):
        inv_d[v] = inv_d.get(v, []) + [k]
    pprint(d)
    print(inv_d)
else:
    print("Invalid input")
    
# Write an algorithm and the subsequent Python code to compute and print the frequency of occurrence of character as a dictionary (ch:count).
