from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check the rows
        for row in board:
            values = [cell for cell in row if cell != "."]
            if len(values) != len(set(values)):
                return False

        # check the columns
        columns = [
            [row[i] for row in board if row[i] != "."] for i in range(len(board[0]))
        ]
        for col in columns:
            if len(col) != len(set(col)):
                return False

        # check the sub-boxes
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        value = board[row_start + i][col_start + j]
                        if value != ".":
                            if value in seen:
                                return False
                            seen.add(value)

        return True


if __name__ == "__main__":
    test = Solution()
    print(
        test.isValidSudoku(
            [
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )
