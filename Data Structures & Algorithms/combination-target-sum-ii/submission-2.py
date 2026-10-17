class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, subset, total):
            if i >= len(candidates):
                if total == target:
                    res.append(subset.copy())
                return
            # if total > target:
            #     #prune this branch
            #     return
            # if total == target:
            #     # can prune
            #     res.append(subset.copy())
            #     return
            
            subset.append(candidates[i])
            if total + candidates[i] < target:
                dfs(i+1, subset, total + candidates[i])
            elif total + candidates[i] == target:
                res.append(subset.copy())
            subset.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, subset, total)
        
        dfs(0, subset, 0)

        return res