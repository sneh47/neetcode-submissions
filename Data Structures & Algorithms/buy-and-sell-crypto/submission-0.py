class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        p = prices[0]
        for price in prices[1:]:
            if price < p:
                p = price
            else:
                maxprof = max(maxprof, price - p)

        return maxprof