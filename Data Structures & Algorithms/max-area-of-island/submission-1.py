class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        num = 0

        visited = set()
        q = deque()

        dirs = [(-1, 0), (1,0), (0,-1), (0,1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited or grid[i][j] == 0:
                    continue
                #only 1s that have not been encountered(new island)
                curarea = 1
                maxarea = max(maxarea, curarea)
                num +=1
                q.append((i,j))
                visited.add((i,j))
                while q:
                    a, b = q.popleft()
                    #print(a,b)
                    for d in dirs:
                        new_a, new_b = a+d[0], b+d[1]
                        if (new_a, new_b) not in visited and 0 <= new_a < len(grid) and 0 <= new_b < len(grid[0]) and grid[new_a][new_b] != 0:
                            #the new direction is not in visited, and a valid coordinate, and is not water
                            q.append((new_a, new_b))
                            visited.add((new_a, new_b))
                            curarea +=1
                            maxarea = max(maxarea, curarea)
        print(num)
        return maxarea