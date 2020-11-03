tic = [list(map(str, input().split())) for _ in range(3)]
if tic[0][0] == 'X' and tic[1][1] == 'X' and tic[2][2] == 'X':
    print("X is the winner!")
    exit()
elif tic[0][0] == 'O' and tic[1][1] == 'O' and tic[2][2] == 'O':
    print("O is the winner!")
    exit()
elif tic[0][2] == 'X' and tic[1][1] == 'X' and tic[2][0] == 'X':
    print("X is the winner!")
    exit()
elif tic[0][2] == 'O' and tic[1][1] == 'O' and tic[2][0] == 'O':
    print("O is the winner!")
    exit()
for i in range(3):
    if tic[i][0] == 'X' and tic[i][1] == 'X' and tic[i][2] == 'X':
        print("X is the winner!")
    elif tic[i][0] == 'O' and tic[i][1] == 'O' and tic[i][2] == 'O':
        print("O is the winner!")
    elif tic[0][i] == 'X' and tic[1][i] == 'X' and tic[2][i] == 'X':
        print("X is the winner!")
    elif tic[0][i] == 'O' and tic[1][i] == 'O' and tic[2][i] == 'O':
        print("O is the winner!")
