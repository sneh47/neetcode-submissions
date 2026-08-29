class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_seq = 0
        for n in nums:
            if n-1 in s:
                continue
            
            c = n
            seq = 1
            while c + 1 in s:
                c+=1
                seq+=1
            if seq > longest_seq:
                longest_seq = seq
        
        return longest_seq