a = tuple(tuple(input() for x in range(8)) for x in range(3))
age_limit, years, skill = int(input()), int(input()), input()
for x in a:
    if int(x[1]) < age_limit and int(x[3]) > years and skill in x:
        print(x[0])
