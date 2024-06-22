# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         nodup=set()
#         for outer in range(len(nums)-2):
#             first_left=nums[outer]
#             second_left=outer+1
#             last=len(nums)-1
#             while(second_left<last):
#                 sec=nums[second_left]
#                 third=nums[last]
#                 summ=first_left+sec+third
            
                    
#                 if(summ>0):
#                     last-=1
#                 elif summ<0:
#                     second_left+=1
#                 else:
#                     nodup.add((first_left,sec,third))
#                     second_left+=1
#                     last-=1
                    
#         return nodup
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res