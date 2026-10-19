class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(map(str, digits))
        plusone = 1 + int(s)
        return list(str(plusone))