class Solution:
    def maxLen(self, n, A):
        # mydict={0:-1}
        # K=0
        # ans=0
        # s=0
        # for i in range(N):
        #     s+=A[i]
            
        #     if s not in mydict:
        #         mydict[s]=i
        #     if s-K in mydict:
        #         ans=max(ans,i-mydict[s-K])
        # return ans
        
        
        
        
        mpp = {}
        maxi = 0
        sum = 0
        for i in range(n):
            sum += A[i]
            if sum == 0:
                maxi = i + 1
            else:
                if sum in mpp:
                    maxi = max(maxi, i - mpp[sum])
                else:
                    mpp[sum] = i
        return maxi
        #Code here