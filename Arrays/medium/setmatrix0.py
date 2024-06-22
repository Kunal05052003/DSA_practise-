import  numpy as np
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        row = [0] * n  # row array
        col = [0] * m  # col array

        # Traverse the matrix:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark ith index of row wih 1:
                    row[i] = 1

                    # mark jth index of col wih 1:
                    col[j] = 1

        # Finally, mark all (i, j) as 0
        # if row[i] or col[j] is marked with 1.
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0

        return matrix



        # if not matrix:
        #     return []

        # m = len(matrix)
        # n = len(matrix[0])

        # zeroes_row = [False] * m
        # zeroes_col = [False] * n
        # a=[]
        # b=[]
        # for row in range(m):
        #     for col in range(n):
        #         if matrix[row][col] == 0:
        #             zeroes_row[row] = True
        #             zeroes_col[col] = True

        # for row in range(m):
        #     for col in range(n):
        #         if zeroes_row[row] or zeroes_col[col]:
        #             matrix[row][col] = 0
        # return matrix
        


    
        # row1=arr[0,:]
        # row2=arr[2:]
        # row3=arr[3:]
        # print(row1)

        """
        Do not return anything, modify matrix in-place instead.
        """
        