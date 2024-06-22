class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        # if(k<=len(nums)):
        #     next=nums[len(nums)-k:]
        #     prev=nums[:len(nums)-k]
        #     ans=next+prev
        #     for i in range(len(ans)):
        #         nums[i]=ans[i]
        # else:
        k=k%len(nums)
        next=nums[len(nums)-k:]
        prev=nums[:len(nums)-k]
        ans=next+prev
        for i in range(len(ans)):
            nums[i]=ans[i]

        
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """