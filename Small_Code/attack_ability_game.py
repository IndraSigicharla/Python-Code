x = list(map(int, input().split()))
y = [list(map(int, input().split())) for _ in range(x[-1])]
sly = sorted(y)
alive = True
dlist = [i[0] for i in sly]
blist = [i[1] for i in sly]
for _ in range(len(dlist)):
    for i, j in enumerate(dlist):
        if j < x[0]:
            x[0] += blist[i]
            dlist.pop(i)
            blist.pop(i)
if len(dlist) != 0:
    alive = False
if alive:
    print("YES")
else:
    print("NO")

# Problem of the Day question:
# ? IronMan is stuck on a level of the Infinity War game which he is playing now.
# ? To advance this level, he has to kill all the N dragons that are present on this level.
# ? IronMan and the dragons have strength, which is represented by an integer.
# ? In the fight between him and dragon, the fight's outcome is determined by their strength.
# ? Initially, IronMan's strength equals S. If IronMan starts dueling with the ith(1 <= i <= N) dragon and IronMan's strength is not greater than the dragon's strength Xi, then IronMan loses the duel and dies.
# ? But if IronMan's strength is greater than the dragon's strength, then he defeats the dragon and gets a bonus strength increase by Yi.
# ! Sample Input 1: 2 2
# !                 1 99
# !                 100 0
# * Output 1: YES

# ! Sample Input 2: 8 1
# !                 100 100
# * Output 1: NO
