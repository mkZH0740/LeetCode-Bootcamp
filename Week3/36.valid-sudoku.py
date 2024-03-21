from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        cells = set()

        for row_index in range(0, 9):
            row = board[row_index]

            for col_index in range(0, 9):
                entry = row[col_index]

                if entry == ".":
                    continue

                row_key = f"{row_index}${entry}"
                if row_key in rows:
                    return False
                rows.add(row_key)

                col_key = f"{col_index}${entry}"
                if col_key in cols:
                    return False
                cols.add(col_key)

                cell_index = (row_index // 3) * 3 + col_index // 3
                cell_key = f"{cell_index}${entry}"
                if cell_key in cells:
                    return False
                cells.add(cell_key)

        return True
