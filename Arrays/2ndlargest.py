def print2largest(self,arr, n):
    s=list(set(arr))
    if len(s)<2:
        return -1
    # z=s.remove(
    else:
        maxx = arr[0]
    
    
        for i in range(0, len(s)):
            if (maxx < s[i]):
                maxx = s[i]
        z=s.remove(maxx)
        ans=max(s)
        return ans
            # code here