import re
vowel_list, consonant_list = [], []
s = input("Enter a sentence: ").split()
s = [_.replace(".", "") for _ in s]
checker = "[aeiouAEIOU]"
for x in range(len(s)):
    if re.search(checker, str(s[x][0])):
        vowel_list.append(s[x])
    else:
      consonant_list.append(s[x])
print(f"The list of words that begin with a vowel are: {vowel_list}")
print(f"The list of words that begin with a consonant are: {consonant_list}")
