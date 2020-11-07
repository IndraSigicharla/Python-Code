w1 = input()
w2 = input()
x = "aeiou"
a = [i for i in w1 if i in x]
for i in a:
    m = w1[:w1.index(i)]
    break
b = [j for j in w2 if j in x]
for j in b:
    n = w2[w2.index(j):]
    break
print(m + n)
