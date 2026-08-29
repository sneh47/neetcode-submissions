class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s = s + str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        while(s != ""):
            l, rest = s.split("#", 1)
            #4#neet4#love
            strs.append(rest[0:int(l)])
            s = rest[int(l):]

        return strs
