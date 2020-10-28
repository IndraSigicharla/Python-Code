# Code
x = "oneliner.py"

f = open(x)
lines = []
for line in f:
    lines.append(line.strip())

print(lines)

# Code in one line:
print([line.strip() for line in open("oneliner.py")])