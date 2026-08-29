class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for c in s:
            if c.isalnum():
                a += c.lower()
        
        l, r = 0, len(a) - 1
        print(a)
        while l < r:
            if a[l] != a[r]:
                return False
            l+=1
            r-=1
        
        return True
        