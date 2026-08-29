class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None] * len(nums)
        left_products = [None] * len(nums)
        right_products = [None] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                left_products[i]=nums[i]
                continue
            left_products[i] = left_products[i-1] * nums[i]

        for i in range(len(nums)-1,-1, -1):
            if i == len(nums)-1:
                right_products[i]=nums[i]
                continue
            right_products[i] = right_products[i+1] * nums[i]
        
        
        for i in range(len(nums)):
            if i == 0:
                output[i] = right_products[1]
                continue
            if i == len(nums) -1:
                output[i] = left_products[len(nums)-1 -1]
                continue
            
            output[i] = left_products[i-1] * right_products[i+1]

        return output