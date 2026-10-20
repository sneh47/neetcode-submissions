import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use max heap of size k - add all points to heap - in the end, only k closest will remain as larger points get evicted from heap pop

        heap = []
        heapq.heapify_max(heap)

        for point in points:
            d = math.sqrt(point[0]*point[0]+point[1]*point[1])
            if len(heap) >= k:
                heapq.heappushpop_max(heap, (d,point))
            else:
                heapq.heappush_max(heap, (d,point))
        
        return [h[1] for h in heap]