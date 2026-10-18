class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = ""

        def dfs(o, c, subset):
            if o+c == 2*n:
                res.append(subset)
                return
            
            if o < n:
                osubset = subset + "("
                dfs(o+1, c, osubset)
            #use subset as backtrack
            if c < o:
                csubset = subset + ")"
                dfs(o, c+1, csubset)
        
        dfs(0, 0, "")
        return res
