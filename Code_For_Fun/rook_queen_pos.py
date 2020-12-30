a = [(x, y) for x in list(range(1, 9)) for y in list(range(1, 9))]
rr, rc = int(input()), int(input())
qr, qc = int(input()), int(input())
ULDR_moves = lambda x, y : [i for i in a if (i[1] == y or i[0] == x) and i != (qr, qc)]
diag = [i for i in a if (i[1] - i[0] == qc - qr or sum(i) == qc + qr) and i != (rr, rc)]
move_set_rook, move_set_queen = ULDR_moves(rr, rc), ULDR_moves(qr, qc)
move_set_queen.extend(diag)
common = list(set(move_set_queen).intersection(set(move_set_rook)))
print(*sorted(common), sep = "\n")

"""Given the position of a Rook and a queen in a chess board (8X8 board),
write an algorithm and the subsequent Python code to determine the common positions where both rook and queen can be placed in the next move."""
