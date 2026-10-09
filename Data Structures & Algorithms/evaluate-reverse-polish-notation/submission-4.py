class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) ==1:
            return int(tokens[0])
        result = None
        stack = []
        for token in tokens:
            if token not in ["+", "-", "/", "*"]:
                stack.append(token)
            else:
                #op
                
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if token == "+":
                    result = op1 + op2
                elif token == "-":
                    result = op1 - op2
                elif token == "*":
                    result = op1 * op2
                else:
                    result = int(op1 / op2)
                stack.append(result)
                #print(result)
                
        
        return result