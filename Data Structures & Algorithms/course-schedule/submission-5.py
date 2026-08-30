class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #dictionary that maps prereq course to dependents
        ht = defaultdict(list)
        indegrees = [0] * numCourses
        for pre in prerequisites:
            ht[pre[1]].append(pre[0])
            indegrees[pre[0]] +=1
        
        q = deque([])
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            c = q.popleft()
            numCourses-=1
            for dep in ht[c]:
                indegrees[dep] -= 1
                if indegrees[dep] == 0:
                    q.append(dep)
        
        if numCourses!=0:
            return False
        return True