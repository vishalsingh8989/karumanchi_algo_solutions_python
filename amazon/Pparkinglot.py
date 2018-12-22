


def solution(matrix):
    """
    """
    
    rows = len(matrix)

    cols = len(matrix[0]) 
    if matrix[0][0] == 0:
        return -1

    queue = [(0,0,0)]

    visited = set()
    
    while queue:
        i, j, steps = queue.pop(0)
        
        if (i,j) not in visited:
            
            
            visited.add((i,j))
            if matrix[i][j] == 9:
                return steps 
            elif matrix[i][j] == 1:
                for x, y in [(1,0), (0,1), (-1,0),(0,-1)]:
                    if 0 <=  i + x < rows and 0 <= j + y < cols and matrix[i + x][j + y] != 0:
                        queue.append((i + x, j + y, steps + 1))
                    
    
    return -1
    
    


if __name__ == "__main__":
    matrix = [[1,1,1,1],
              [0,1,1,1],
              [0,1,0,1],
              [1,1,9,1],
              [0,0,1,1]
              ]
    
    print(solution(matrix))
    
    matrix = [[1,0,0],
              [1,0,0],
              [1,9,1]]
 
    print(solution(matrix))
                    
                    
                    