class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify_max(nums)
        self.heap = nums
        #print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[-1]
