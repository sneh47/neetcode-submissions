class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = []

        s = 0
        while True:
            while n > 0:
                d = n % 10
                n = n//10
                s += d*d
            if s == 1:
                return True
            else:
                if s in numbers:
                    return False
                numbers.append(s)
            n = s
            s = 0
