class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        m = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        res = []

        def dfs(i, s):
            if i == len(digits):
                res.append(s)
                return
            
            
            number = int(digits[i])
            for c in m[number]:
                new_s = s + c
                dfs(i+1, new_s)
        
        dfs(0, "")

        return res