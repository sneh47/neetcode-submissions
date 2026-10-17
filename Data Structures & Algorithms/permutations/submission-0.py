class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                
                if nums[i] not in subset:
                    subset.append(nums[i])
                    dfs()
                    subset.pop()
                    
            
        

        dfs()
        return res