from src.piece import Piece

class Queen(Piece):
    def char(self):
        return 'Q'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        if row == row_1:
            return all(board.get_piece(row, c) is None for c in range(min(col, col_1) + 1, max(col, col_1)))
        if col == col_1:
            return all(board.get_piece(r, col) is None for r in range(min(row, row_1) + 1, max(row, row_1)))
        diff_row = abs(row - row_1)
        diff_col = abs(col - col_1)
        if diff_row == diff_col:
            return all(board.get_piece(row + i, col + i) is None for i in range(1, diff_row))
        return False

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)