#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        #Complete the function
        mydict={0:-1}
        ans=0
        s=0
        for i in range(N):
            s+=A[i]
            
            if s not in mydict:
                mydict[s]=i
            if s-K in mydict:
                ans=max(ans,i-mydict[s-K])
        return ans

