class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        # # nums.sort()
        # # s=list(set(nums))
        # # s.sort()
        # # c=1
        # # m=1
        # d={}
    
        # for i in range(1,len(s)):
        #     if(s[i]-s[i-1]==1):
        #         c+=1
        #         m=max(c,m)
        #     else:
        #         c=1

        # if(len(nums)==0):
        #     return 0
        # return m
        n = len(a)
        if n == 0:
            return 0

        longest = 1
        st = set()
        # put all the array elements into set
        for i in range(n):
            st.add(a[i])

        # Find the longest sequence
        for it in st:
            # if 'it' is a starting number
            if it - 1 not in st:
                # find consecutive numbers
                cnt = 1
                x = it
                while x + 1 in st:
                    x += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest
