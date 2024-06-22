import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # ans = []
        # for i in range(numRows):
        #     ans.append([1] * (i+1))
        #     for j in range(1, i):
        #         ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        # return ans
        s=[]
    
        n=numRows
        for j in range(n):
            d=[1]

            for i in range(1,j+1):
                d.append(math.comb(j,i))
            s.append(d)
        print(s)
            

        
        return s