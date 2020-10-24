from itertools import accumulate
m = int(input())
n = int(input())
acc1 = [1]
acc2 = [1]
acc1.extend([m]*100)
acc2.extend([n]*100)
x = list(accumulate(acc1))
y = list(accumulate(acc2))
x[:] = [l for l in x if l <= 31]
y[:] = [l for l in y if l <= 31]
inter = set(x).intersection(set(y))
print(len(inter))
