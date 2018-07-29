

def Knows(matrix, i, j):
    return matrix[i][j]


def findCelebrity(matrix):
    stack = []
    
    
    for i in range(len(matrix)):
        stack.append(i)
    
    a = stack.pop()
    b = stack.pop()
    
    
    while len(stack) > 1:
        if Knows(matrix, a, b):
            stack.append(b)
        elif Knows(matrix, b, a):
            stack.append(a)
        
        a = stack.pop()
        b = stack.pop()
            

    print(stack)
if __name__ == "__main__":
    matrix = [[0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 1, 0]]
    
    findCelebrity(matrix)