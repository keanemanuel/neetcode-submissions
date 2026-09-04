from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. check rows
        for rows in board:
            seen = set()
            for num in rows:
                if num in seen:
                    return False
                if num.isdigit():
                    seen.add(num)

        # 2. check cols
        for rows in range(9):
            seen = set()
            for cols in range(9):
                num = board[cols][rows]
                if num in seen:
                    return False
                if num.isdigit():
                    seen.add(num)     

        # 3. check 3*3
        squares = defaultdict(set)
        for rows in range(9):
            for cols in range(9):
                num = board[cols][rows]
                if num in squares[(rows // 3, cols // 3)]:
                    return False
                if num.isdigit():
                    squares[(rows // 3, cols // 3)].add(num)
        return True