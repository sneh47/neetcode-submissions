class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return [0]
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
                continue
            if temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    _, idx = stack.pop()
                    result[idx] = i - idx
                stack.append((temperatures[i], i))
        
        return result