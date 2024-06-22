class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, a):
        m=a[-1]
        ans=[a[-1]]
        for i in range(len(a)-2,-1,-1):
            if a[i]>=m:
                ans.append(a[i])
                m=a[i]
        #Code here
        x=ans[::-1]
        return x