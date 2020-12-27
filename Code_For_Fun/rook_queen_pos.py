def cartesian(*lsts):
    result = [[]]
    for target in list(map(tuple, lsts)):
        result = [x + [y] for x in result for y in target]
    for product in result:
        yield tuple(product)
a = list(range(1, 9))
rookRow, rookColumn = int(input()), int(input())
queenRow, queenColumn = int(input()), int(input())
def UDLR_moves(x, y):
    c1 = set(cartesian([x], a))
    c2 = set(cartesian(a, [y]))
    return list(c1.union(c2))
diag = [(x, y) for x, y in list(cartesian(a, a)) if y - x == queenColumn - queenRow or y + x == queenColumn + queenRow]
move_set_rook = UDLR_moves(rookRow, rookColumn)
move_set_queen = UDLR_moves(queenRow, queenColumn)
move_set_queen.extend(diag)
common = list(set(move_set_queen).intersection(set(move_set_rook)))
if (rookRow, rookColumn) in common:
    common.remove((rookRow, rookColumn))
if (queenRow, queenColumn) in common:
    common.remove((queenRow, queenColumn))
for i in sorted(common):
    print(i)

"""Given the position of a Rook and a queen in a chess board (8X8 board),
write an algorithm and the subsequent Python code to determine the common positions where both rook and queen can be placed in the next move."""
