ops = ["*" , "/" , "-", "+", "^"]


def postfixtoinfix(expression):
    stack = []
    for charac in expression:
        if charac not in ops:
            stack.append(charac)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            res = "(" + op1 + charac + op2 +  ")"
            stack.append(res)
    
    return stack.pop()

if __name__ == "__main__":
    expression = {"abc++" : "(a+(b+c))",
                  "ab*c+" : "((a*b)+c)"
                  }
    
    res = []
    for key, val in expression.iteritems():
        res.append(val == postfixtoinfix(key))
    
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
        