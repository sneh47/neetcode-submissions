class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i in range(len(nums)):
            if target - nums[i] in ht:
                s = ht[(target-nums[i])]
                return[s, i]
            if nums[i] not in ht:
                ht[nums[i]] = i
            
            
        