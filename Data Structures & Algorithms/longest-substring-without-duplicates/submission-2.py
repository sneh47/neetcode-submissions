class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ht = {}
        max_count = 0

        for r in range(len(s)):
            if s[r] in ht:
                l = max(ht[s[r]]+ 1, l)

            ht[s[r]] = r
            max_count = max(max_count, r - l + 1)

        return max_count