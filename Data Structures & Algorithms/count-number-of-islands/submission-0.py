class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        visited = set()
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(i, j, grid[i][j])
                if (i,j) in visited:
                    continue
                if grid[i][j] == '0':
                    visited.add((i,j))
                else:
                    q.append((i, j))
                    print(i, j, grid[i][j])
                    num +=1
                    while q:
                        a, b = q.pop(0)
                        if(a, b) in visited:
                            continue
                        visited.add((a,b))
                        up = a-1
                        down = a+1
                        left = b-1
                        right = b+1
                        if up >= 0 and (up,b) not in q and (up,b) not in visited:
                            if grid[up][b] == '0':
                                visited.add((up,b))
                            elif grid[up][b] == '1':
                                q.append((up, b))
                        if down < len(grid):
                            if (down,b) in q or (down,b) in visited:
                                pass
                            elif grid[down][b] == '0':
                                visited.add((down,b))
                            elif grid[down][b] == '1':
                                q.append((down, b))
                        if left >= 0:
                            if (a,left) in q or (a,left) in visited:
                                pass
                            elif grid[a][left] == '0':
                                visited.add((a,left))
                            elif grid[a][left] == '1':
                                q.append((a, left))
                        if right < len(grid[0]):
                            if (a,right) in q or (a,right) in visited:
                                pass
                            elif grid[a][right] == '0':
                                visited.add((a,right))
                            elif grid[a][right] == '1':
                                q.append((a, right))
        
        return num