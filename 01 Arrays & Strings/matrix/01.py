# return snake sum 
# 
def snakeMatrix(matrix: list[list[int]]) -> list[int]:
    res = []
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)
    
    while left < right and top<bottom:
        for i in range(left, right):
            # print(matrix[top][i])
            res.append(matrix[top][i])
        top +=1        
        
        # down one level
        for i in range(top,bottom-1):
            res.append(matrix[i][right -1])
        right-=1
    
        if not left >= right and top >= bottom:
            break

       
        for i in range(right-1, left-1,-1):
            res.append(matrix[top][i])
        top+=1
        right+=1
        
        # left+=1
        
    
    return res

print(snakeMatrix([[1,2,3],[4,5,6],[7,8,9]]))
print(snakeMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
