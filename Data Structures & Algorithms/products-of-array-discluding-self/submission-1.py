class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        

        #compute prefix in output
        for i in range(1, len(output)):
            output[i] = output[i-1] * nums[i-1]

        suffix_prod = 1
        #multiply suffix with each prefix in output
        for i in range(len(output) -1 , -1 , -1):
            output[i] = output[i] * suffix_prod
            suffix_prod *= nums[i]
        return output