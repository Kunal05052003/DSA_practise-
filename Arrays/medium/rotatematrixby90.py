import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # self.matrix = matrix
        # self.n = len(matrix)
        # b=self.matrix[::-1]
        # arr = np.array(b)
        # t=arr.transpose()

        # for i in range(self.n):
        #     for j in range(self.n):
        #         self.matrix[i][j]=t[i][j]




        
 
        n = len(matrix)
        # transposing the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversing each row of the matrix
        for i in range(n):
            matrix[i].reverse()







        # for i in range(self.n):
        #     self.matrix[i]= self.matrix[::-1][i]
        # self.matrix[i][j]
      
        
        # for i in range(self.n):
        #     for j in range(i + 1, self.n):
        #         self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i],self.matrix[i][j]
        
        #
        
        
        """
        Do not return anything, modify matrix in-place instead.
        """