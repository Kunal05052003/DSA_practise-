class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=len(nums)+1
        x=len(nums)
        z=(x*s)//2
        print(z)
        v=sum(nums)
        return abs(v-z)
        # a=list(range(0,len(nums)+1))
        # b=set(a)
        # for i in nums:
        #     if i not in nums:
        #         return i

        # print(a)