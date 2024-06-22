class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        # l=0
        # r=1
      

        # while(r<len(prices)):
        #     if(prices[r]>prices[l]):
        #         maxx=max(maxx,prices[r]-prices[l])
        #         r+=1

        #     else:
        #         l=r
        #         r+=1
        # return(maxx)



        m=max(prices)

        for i in range(len(prices)):
            m=min(m,prices[i])
            p = max(p,prices[i]-m)
        
        return p