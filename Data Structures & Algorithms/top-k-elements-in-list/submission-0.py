class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = collections.defaultdict(int)
        for num in nums:
            freq_table[num] +=1
        


        output = []
        while k != 0:
            max_num = -1
            max_freq = -1
            for num in freq_table:
                if freq_table[num] > max_freq and num not in output:
                    max_num = num
                    max_freq = freq_table[num]
            output.append(max_num)
            k-=1

        return output