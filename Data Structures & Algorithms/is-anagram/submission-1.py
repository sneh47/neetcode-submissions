from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = Counter()
        for c in s:
            cnt[c] +=1
        
        for c in t:
            cnt[c] -=1
        total = 0
        for v in cnt.values():
            if v !=0:
                return False
        return True