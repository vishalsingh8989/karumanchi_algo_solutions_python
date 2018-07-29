

open_bracket = "{[("
close_bracket = "}])"
bracket = open_bracket + close_bracket
priority = {'+':1, '-':1, '*':2, '/':2, '^':3}


def islessthanequalto(a, b):
    if priority[a] >= priority[b]:
        return True
    else:
        return False

def infixtoprefix(expression):
    expression = expression[::-1]
    expression = expression.replace("(", "@")
    expression = expression.replace(")", "$")
    expression = expression.replace("@", ")")
    expression = expression.replace("$", "(")
    
    stack = []
    res = ""
    for charac in expression:
        if charac.isalpha():
            res = res + charac
        elif charac == "(":
            stack.append(charac)
        elif charac == ")":
            while stack and stack[-1] != "(":
                res = res + stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and islessthanequalto(stack[-1], charac):
                res = res + stack.pop()
            stack.append(charac)
        
    
    while stack:
        res = res + stack.pop()
    
    return res[::-1]
            
                
    

if __name__ == "__main__":
    expression = {"A*B+C/D" : "+*AB/CD",
                  "(A-B/C)*(A/K-L)" : "*-A/BC-/AKL",
                  "(AX*(BX*(((CY+AY)+BY)*CX)))" : "*AX*BX*++CYAYBYCX",
                  "((H*((((A+((B+C)*D))*F)*G)*E))+J)":"+*H***+A*+BCDFGEJ"
                  }
    
    #expression = "A*B+C/D"
    res = []
    for key,  val in expression.iteritems():
        res.append(val == infixtoprefix(key))
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    
