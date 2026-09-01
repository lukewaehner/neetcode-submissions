class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                # 0, 0 = box 0 
                # 8, 8 = box 8

                bid = (r//3) * 3 + (c//3)
                
                if val in rows[r] or val in cols[c] or val in boxes[bid]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[bid].add(val)
        return True