from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if (
                    num in rows[row] or
                    num in cols[col] or 
                    num in grid[(row // 3, col // 3)]
                    ):
                    return False

                if num.isdigit():
                    cols[col].add(num)  
                    rows[row].add(num)
                    grid[(row // 3, col // 3)].add(board[row][col])
        return True