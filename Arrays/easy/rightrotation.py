k=k%len(nums)
next=nums[k:]
prev=nums[:k]
ans=next+prev
for i in range(len(ans)):
    nums[i]=ans[i]