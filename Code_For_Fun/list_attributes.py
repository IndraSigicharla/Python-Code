my_list = []
a = [list(map(str, input().split())) for x in range(int(input()))]
for x, i in enumerate(a):
    if i[0] == "insert":
        my_list.insert(int(i[1]), int(i[2]))
    elif i[0] == "print":
        print(my_list)
    elif i[0] == "remove":
        my_list.remove(int(i[1]))
    elif i[0] == "append":
        my_list.append(int(i[1]))
    elif i[0] == "sort":
        my_list.sort()
    elif i[0] == "pop":
        my_list.pop()
    elif i[0] == "reverse":
        my_list.reverse()
