class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d_r = collections.defaultdict(set)
        d_c = collections.defaultdict(set)
        d_s = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in d_r[r] or board[r][c] in d_c[c] or board[r][c] in d_s[(r//3, c//3)]:
                    return False
                d_r[r].add(board[r][c])
                d_c[c].add(board[r][c])
                d_s[(r//3,c//3)].add(board[r][c])

        return True

                

