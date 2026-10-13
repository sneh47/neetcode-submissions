import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpile = max(piles)
        #[0, 1 ,2 , ..., maxpile] sorted non-decreasing array
        #maxpile will obviously eat all piles in an hour each, maxpile hours which should be less than h hours
        #can we go lower, how lower, we should binary search the array to find the hour amount
        #will need a subroutine to calculate the k for each hour amount

        left = 1 #banana per hour
        right = maxpile

        while left <= right:
            mid = (left + right) // 2

            #calc hours
            amount = 0
            for pile in piles:
                amount += math.ceil(pile/mid)
            
            if amount <= h:
                #valid, can you eat less and still be valid
                right = mid - 1
            
            else:
                #too many hours, need to eat more
                left = mid + 1
        
        print(left, mid, right)
        return left