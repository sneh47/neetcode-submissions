class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqcount = [0] * numCourses
        ht = defaultdict(list)
        for prereq in prerequisites:
            ht[prereq[1]].append(prereq[0])
            #as an example, course prereq[0] has 1 more prereq in prereq[1]
            prereqcount[prereq[0]] += 1
        
        q = deque([])
        for i in range(numCourses):
            if prereqcount[i] == 0:
                q.append(i)
        
        while q:
            courseNo = q.popleft()
            numCourses-=1
            #take this courseNo off the other courses, if they have no other courses then add to q
            for c in ht[courseNo]:
                #decrement this course by 1
                prereqcount[c] -=1
                if prereqcount[c] == 0:
                    q.append(c)
            
        if numCourses != 0:
            return False
        return True