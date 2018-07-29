

ops = ["*" , "/" , "-", "+", "^"]

def postfixtoinfix(expression):
    res = ""
    stack = []
    for i in xrange(len(expression) - 1, -1 , -1):
        #print(expression[i])
        if expression[i] in ops:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append("(" + op1 + "" + expression[i] + "" + op2 + ")")
        else:
            stack.append(expression[i])
    return stack.pop()

if __name__ == "__main__":
    expression = "*+AB-CD"
    print(postfixtoinfix(expression))
    expression =  "*-A/BC-/AKL"
    print(postfixtoinfix(expression))
    
    print(postfixtoinfix(expression))