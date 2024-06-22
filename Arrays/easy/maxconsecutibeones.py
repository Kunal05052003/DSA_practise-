class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        l=0
        zeros= 0
        for right, n in enumerate(nums):
            # print(right,n)
            zeros += n == 0
            # print(zeros)
            if zeros > 0: # here k instead of 0
                zeros -= nums[l] == 0
                l += 1
        return right - l + 1



        # ********brute force ****************
        # c = 0
        # a = 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         c += 1
        #         a=max(a,c)
        #     else:
                
        #         c = 0
        
        # return a