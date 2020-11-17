import re
a = [i for i in input().replace(",", " ").replace(".", " ").replace("_", " ").split() if re.search(r"^\w+\[{1}[A-Z]+\-{1}\d+\]{1}", i)]


def tag(x):
    for i in x:
        m = i.replace("[", " ")
        n = m.replace("]", "")
        print(n)


if len(a) == 0:
    print(-1)
else:
    tag(a)
# Test Case

"""
gafkjen[ABC-123] this is some test data,[ABC-2131]klsd final Lorem ipsum dolor sit amet, consectetur adipiscing[TEST-1234],elit, sed do eiusmod tempor incididunt ut labore et doloremagna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate[ID-2341] velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
