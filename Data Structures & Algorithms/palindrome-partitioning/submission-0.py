class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        
        def dfs(start):
            if start == len(s):
                res.append(subset.copy())
                return
            
            for i in range(start, len(s)):
                a = s[start:i+1]

                left = 0
                right = len(a) - 1
                palindrome = True
                while left < right:
                    if a[left] != a[right]:
                        palindrome = False
                        break
                    left +=1
                    right -=1

                if palindrome:
                    subset.append(a)
                    dfs(i+1)
                    subset.pop()
        
        dfs(0)
        return res