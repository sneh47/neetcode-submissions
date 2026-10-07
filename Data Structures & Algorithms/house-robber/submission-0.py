class Solution:
    def rob(self, nums: List[int]) -> int:
        best = 0
        prevbest = 0
        for i in range(len(nums)):
            newbest = max(nums[i]+prevbest, best)
            
            prevbest = best
            best = newbest

        return best