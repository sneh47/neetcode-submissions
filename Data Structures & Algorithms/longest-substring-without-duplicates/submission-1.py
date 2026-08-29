class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #zxyxza
        if len(s) == 0:
            return 0
        
        l = 0
        r = 0
        maxlen = 1
        ht = {} # k = letter v = index?
        while r < len(s):
            if s[r] not in ht:
                ht[s[r]] = r

                maxlen = max(maxlen, r-l+1)
                r+=1
            else:
                while s[l] != s[r]:
                    
                    del ht[s[l]]
                    l+=1
                del ht[s[l]]
                l+=1
        
        return maxlen
                