
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # mydict={0:-1}
        # N=len(A)
        # ans=0
        # s=0
        # for i in range(N):
        #     s+=A[i]
            
        #     if s not in mydict:
        #         mydict[s]=i
        #     if s-K in mydict:
        #         ans+=1
        # return ans
        ps=0
        s=Counter()
        s[0]=1
        c=0
        print(nums)
        for i in nums:
            ps+=i
            print(ps)
            c+=s[ps-k]
            print(c)
            s[ps]+=1
        print(s)    
        return c
        # for i in range(len(A)):
        #     ps+=A[i]
        #     if(ps==K):
        #         c+=1
        #     if((ps-K) in s):
        #         c+=1

        #     s.append(ps)
        # return c