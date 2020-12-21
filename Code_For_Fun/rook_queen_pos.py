from itertools import *
a = [i for i in range(1, 9)]
ALL = list(product(a, a))
diag = []
rr = int(input())
rc = int(input())
qr = int(input())
qc = int(input())
def moveLine(x, y):
    c1 = set(product([x], a))
    c2 = set(product(a, [y]))
    return list(c1.union(c2))
def Diag(lst):
    for x, y in lst:
        if y - x == qc - qr or y + x == qr + qc:
            diag.append((x, y))
move_set_rook = moveLine(rr, rc)
move_set_queen = moveLine(qr, qc)
Diag(ALL)
move_set_queen.extend(diag)
common = list(set(move_set_queen).intersection(set(move_set_rook)))
if (rr, rc) in common:
    common.remove((rr, rc))
if (qr, qc) in common:
    common.remove((qr, qc))
for i in sorted(common):
    print(i)

"""Given the position of a Rook and a queen in a chess board (8X8 board),
write an algorithm and the subsequent Python code to determine the common positions where both rook and queen can be placed in the next move."""
