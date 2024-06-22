from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numMap = {}
        # n = len(nums)

        # # Build the hash table
        # for i in range(n):
        #     numMap[nums[i]] = i
        # print(numMap)
    






        f=[]
        c={}
        for i in range(len(nums)):
            ans=target-nums[i]
            if ans in c:
                return [c[ans],i]
            c[nums[i]]=i
        return []

        # final=[]
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j]==target):
        #             final.append(i)
        #             final.append(j)
                
        #             break
        # return(final)
                    

            