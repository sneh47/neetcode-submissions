class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for s in strs:
            m = [0] * 26
            for c in s:
                m[ord(c) - 97] +=1
            t = tuple(m)
            if t in ht:
                ht[t].append(s)
            else:
                ht[t] = [s]
        out = []
        for v in ht.values():
            out.append(v)
        return out