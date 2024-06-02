from src.piece import Piece

class King(Piece):
    def char(self):
        return 'K'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        diff_row = abs(row - row_1)
        diff_col = abs(col - col_1)
        if diff_row <= 1 and diff_col <= 1:
            return board.get_piece(row_1, col_1) is None or board.get_piece(row_1, col_1).color != self.color
        return False

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)