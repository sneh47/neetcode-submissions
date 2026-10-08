class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        best = 0
        prevbest = 0
        for i in range(1, len(nums)):
            newbest = max(prevbest + nums[i], best)
            prevbest = best
            best = newbest
        bestB = best
        best = 0
        prevbest = 0
        for i in range(0, len(nums)-1):
            newbest = max(prevbest + nums[i], best)
            prevbest = best
            best = newbest
        bestA = best

        
        return max(bestA, bestB)