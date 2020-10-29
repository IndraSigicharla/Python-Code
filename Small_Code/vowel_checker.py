import re
s = input("Enter a sentence: ").split()
checker = "[aeiouAEIOU]"
for item in s:
    if re.search(checker, str(item[0])):
        print(item)
