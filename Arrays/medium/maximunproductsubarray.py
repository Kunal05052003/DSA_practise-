class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx=float('-inf')
        curr=1
        for i in range(len(nums)):
            curr=curr*nums[i]
            maxx=max(curr,maxx)
            if(curr==0):
                curr=1
        curr=1
        for i in range(len(nums)-1,-1,-1):
            curr=curr*nums[i]
            maxx=max(curr,maxx)
            if(curr==0):
                curr=1
        return maxx
        
            