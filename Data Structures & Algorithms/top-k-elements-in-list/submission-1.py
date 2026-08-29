class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = collections.defaultdict(int)
        for num in nums:
            freq_table[num] +=1
        
        
        count = [[] for i in range(len(nums)+1)]
        for num in freq_table:
            count[freq_table[num]].append(num)

        output = []
        current_k = k
        for c in range(len(count) -1 , -1, -1):
            for num in count[c]:
                output.append(num)
                k-=1
                if k == 0:
                    break
            if k==0:
                break

        
        

        return output