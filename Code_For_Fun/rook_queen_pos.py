a = list(range(1, 9))
rr = int(input())
rc = int(input())
qr = int(input())
qc = int(input())
def cartesian(*args, **kwargs):
    targets = list(map(tuple, args)) * kwargs.get('re', 1)
    result = [[]]
    for target in targets:
        result = [x + [y] for x in result for y in target]
    for prod in result:
        yield tuple(prod)
def moveLine(x, y):
    c1 = set(cartesian([x], a))
    c2 = set(cartesian(a, [y]))
    return list(c1.union(c2))
diag = [(x, y) for x, y in list(cartesian(a, a)) if y - x == qc - qr or y + x == qr + qc]
move_set_rook = moveLine(rr, rc)
move_set_queen = moveLine(qr, qc)
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
