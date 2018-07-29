

def prefixtopostfix(expression):
    stack = []
    expression = expression[::-1]
    for charac in expression:
        if charac in "*+-/^":
            op1 = stack.pop()
            op2 = stack.pop()
            res = op1 + op2 + charac
            stack.append(res)
        else:
            stack.append(charac)
        
    return stack.pop()

if __name__ == "__main__":
    expression = {"*+AB-CD" : "AB+CD-*",
                  "*-A/BC-/AKL":"ABC/-AK/L-*",
                  "-*-+abc/ef-g/hi":"ab+c-ef/*ghi/--"
        }
    
    res = []
    for key, val in expression.iteritems():
        res.append(val == prefixtopostfix(key))
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
        