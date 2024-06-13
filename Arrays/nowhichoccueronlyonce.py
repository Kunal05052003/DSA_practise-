
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        
        c=Counter(nums)
        for i,j in c.items():
            if(j==1):
                return i
# ///////////////////////
def getSingleElement(arr):
    # XOR all the elements:
    xorr = 0
    for num in arr:
        xorr ^= num
    return xorr

def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)

if __name__ == "__main__":
    main()



