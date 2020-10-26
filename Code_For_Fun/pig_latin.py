sent = input()
s = sent.split()
sent = []
vchecker = "aeiouAEIOU"
for x in s:
    if x[0] in vchecker:
        sent.append(x + 'way')
    else:
        for y in x:
            if y in vchecker:
                sent.append(x[x.index(y):] + x[:x.index(y)] +'ay')
print(" ".join(sent))
