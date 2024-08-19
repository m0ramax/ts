# # 48. Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

def rotate(matrix: list[list[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.
        left, right = 0, len(matrix) -1
        
        while left < right:
                for i in range(right-left):
                    print(i)
                    top, bottom = left, right

                    # save top left
                    topLeft = matrix[top][left+i]

                    # move bottom left into top left
                    matrix[top][left+i] = matrix[bottom-i][left]

                    # move bottom right into bottom left
                    matrix[bottom-i][left] =matrix[bottom][right - i]

                    # move top right into bottom right
                    matrix[bottom][right -i] = matrix[top+i][right]

                    # move top left into top right
                    matrix[top+i][right] = topLeft
                right-=1
                left +=1
        print(matrix)
                
         
        # top+=1
        # while top < bottom:
        #     for i in range(len(matrix)-1, -1, -1):
        #         row.append(matrix[i][bottom-1])
        #         if len(row) == len(matrix):
        #             #  print(row)
        #              matrix.append(row)
        #              print(matrix)
        #         # print('i ->',i, row)
        #     bottom-=1
                # matrix.insert(0,row)
        # print(matrix)
rotate([[1,2,3],[4,5,6],[7,8,9]])
# rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])