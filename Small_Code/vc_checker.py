import re
vowel_list, consonant_list = [], []
s = input("Enter a sentence: ").split()
s = [_.replace(".", "") for _ in s]
checker = "[aeiouAEIOU]"
for item in s:
    if re.search(checker, str(item[0])):
        vowel_list.append(item)
    else:
        consonant_list.append(item)
print(f"The list of words that begin with a vowel are: {vowel_list}")
print(f"The list of words that begin with a consonant are: {consonant_list}")
