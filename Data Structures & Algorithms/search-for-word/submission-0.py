class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(i, j, word):
            if (i, j) in visited:
                #has been visited
                return False
            if len(word) == 1 and board[i][j] == word:
                #got the whole word in this branch
                return True
            if board[i][j] != word[0]:
                return False

            #valid path but not end
            
            visited.add((i, j))
            #recurse down checking sides
            up = (i-1, j)
            down = (i+1, j)
            right = (i, j+1)
            left = (i, j-1)

            if up[0] >= 0:
                if dfs(i-1, j, word[1:]):
                    return True
            if down[0] < len(board):
                if dfs(i+1, j, word[1:]):
                    return True
            if right[1] < len(board[i]):
                if dfs(i, j+1, word[1:]):
                    return True
            if left[1] >= 0:
                if dfs(i, j-1, word[1:]):
                    return True
            
            #did not find a valid branch, remove from visited so future branches can check this letter
            visited.remove((i,j))
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, word):
                    return True
        return False