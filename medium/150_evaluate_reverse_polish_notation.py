class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if i.isdigit():
                stack.append(int(i))
                print(i)
            elif i[0] == "-" and len(i) > 1:
                stack.append(int(i))
                print(i)
            else:
                if i == "+":
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                    res = a + b
                    print(i)
                    print("res = " + str(res))
                    stack.append(res)
                    print("stack: " + str(stack))
                elif i == "-":
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                    res = b - a
                    print(i)
                    print("res = " + str(res))
                    stack.append(res)
                    print("stack: " + str(stack))
                elif i == "*":
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                    res = a * b
                    print(i)
                    print("res = " + str(res))
                    stack.append(res)
                    print("stack: " + str(stack))
                else:
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                        
                    if a < 0:
                        res = b // -a
                        res = -res
                    elif b < 0:
                        res = -b // a
                        res = -res
                    else:
                        res = b // a

                    print(i)
                    print("res = " + str(res))
                    stack.append(res)
                    print("stack: " + str(stack))
        return stack[0]
