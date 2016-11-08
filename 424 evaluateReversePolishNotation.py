class Solution:
    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        # Write your code here
        
        if len(tokens) < 3:return eval(tokens[0])
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ['+','-','*','/']:
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                op = tokens[i]
                
                if op == '+':
                    stack.append(a+b)
                elif op == '-':
                    stack.append(b-a)
                elif op == '*':
                    stack.append(b*a)
                elif op == '/':
                    if b*a < 0:
                        stack.append(-(-b/a))
                    else:
                        stack.append(b/a)
        return stack.pop()