import re
s = input("Enter a sentence: ").split()
checker = "[aeiouAEIOU]"
for x in range(len(s)):
    if re.search(checker, str(s[x][0])):
        print(s[x])
