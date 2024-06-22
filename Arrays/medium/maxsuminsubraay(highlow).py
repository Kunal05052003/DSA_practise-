
class Solution:
    def pairWithMaxSum(self, arr, N):
        m=0
        for i in range(1,N):
            m=max(m,arr[i]+arr[i-1])
        return m
        # Your code goes here
    