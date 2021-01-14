a = [(x, y) for x in range(1, 9) for y in range(1, 9)]
rr, rc, qr, qc = (int(input()) for _ in range(4))
ULDR_moves = lambda x, y : {i for i in a if (i[1] == y or i[0] == x) and i != (qr, qc)}
move_set_rook, move_set_queen = ULDR_moves(rr, rc), ULDR_moves(qr, qc)
move_set_queen.update({i for i in a if (i[1] - i[0] == qc - qr or sum(i) == qc + qr) and i != (rr, rc)})
print(*sorted(list(move_set_queen.intersection(move_set_rook))), sep = "\n")

"""Given the position of a Rook and a queen in a chess board (8X8 board),
write an algorithm and the subsequent Python code to determine the common positions where both rook and queen can be placed in the next move."""
