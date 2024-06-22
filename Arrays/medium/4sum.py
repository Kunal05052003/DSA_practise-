class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,len(nums)):
                if j!=i+1 and nums[j-1]==nums[j]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    s = nums[i]+nums[j]+nums[k]+nums[l]
                    if s == target:
                        ans.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif s>target:
                        l-=1
                    else:
                        k+=1
        return ans
                 