class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0

        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            #print(fast, slow)
            if fast == slow:
                break
            
        #print("")
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            #print(slow2, slow)
            if slow == slow2:
                return slow
