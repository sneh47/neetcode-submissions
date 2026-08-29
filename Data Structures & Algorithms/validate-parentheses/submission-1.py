class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stk.append(c)
            else:
                if len(stk) == 0:
                    return False
                check = stk.pop()
                if c == ')':
                    if check != '(':
                        return False
                if c == '}':
                    if check != '{':
                        return False
                if c == ']':
                    if check != '[':
                        return False
        if len(stk) !=0:
            return False
        return True
        