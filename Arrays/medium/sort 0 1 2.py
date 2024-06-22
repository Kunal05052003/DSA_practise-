class Solution:
    def sortColors(self, arr: List[int]) -> None:
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        # zero,one,two=[],[],[]
        # for i in range(len(nums)):
        #     if(nums[i]==0):
        #         zero.append(nums[i])
        #     elif(nums[i]==1):
        #         one.append(nums[i])
        #     else:
        #         two.append(nums[i])
        # final=zero+one+two
        # for i in range(len(nums)):
        #     nums[i]=final[i]
        return arr
        
        """
        Do not return anything, modify nums in-place instead.
        """