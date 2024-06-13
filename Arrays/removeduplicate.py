class Solution:
    def removeDuplicates(self, nums: List[int], k = 1) -> int:
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:            # detect next unique value 
                nums[k] = nums[i]               # move it to the end of deduplicated array
                k += 1          
        return k
                        # update the size of deduplicated array
        # m=list(set(nums))
        # m.sort()
        # l=len(m)
        # return l+1