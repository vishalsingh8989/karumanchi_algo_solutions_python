


def postfixtoprefix(expression):
    stack = []
    
    for charac in expression:
        if charac in "+-/*^":
            op2 = stack.pop()
            op1 = stack.pop()
            res = charac +  op1 + op2
            stack.append(res)
        else:
            stack.append(charac)
    
    return stack.pop()


if __name__ == "__main__":
    expression = {"AB+CD-*" : "*+AB-CD",
                  "ABC/-AK/L-*" : "*-A/BC-/AKL" 
                  }
    
    res = []
    for key, val in expression.iteritems():
        res.append(val == postfixtoprefix(key))
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))