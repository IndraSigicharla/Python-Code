x = input().lower()
d = int(input())
cypher = ""
for i in range(len(x)):
    y = x[i]
    cypher += chr((ord(y) + d - 97) % 26 + 97)
print(cypher)

# *In Caesar cipher, each letter is replaced by another letter which occurs at the  d-th position (when counted from the position of the original letter),  in the  English alphabet.
# *For identifying the position of a letter, we follow the usual order of the English alphabet, from a to z.
# *Given a word and a positive integer d, use Caesar cipher to encrypt it.
# *For example, if the word is 'ball' and the value of 'd' is 3 then the new encrypted word is 'edoo'. 'x' will be replaced by 'a', 'y' should be replaced by 'b' and 'z' should be replaced by 'c'.
# *While the code is submitted for Online Judge (SkillRack), use rstrip(), to remove carriage return character in the input.