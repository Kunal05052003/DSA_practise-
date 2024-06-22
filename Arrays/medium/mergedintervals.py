class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        i=0
        arr.sort()
        ans=[]
        for i in range(len(arr)):
           # lie in the last interval:
            if not ans or arr[i][0] > ans[-1][1]:
                ans.append(arr[i])
            # if the current interval
            # lies in the last interval:
            else:
                ans[-1][1] = max(ans[-1][1], arr[i][1])
        return ans

        # if len(intr)==0:
        #     return []
        # elif len(intr)==1:
        #     return list(intr)
        # else:
        #     while i<len(intr)-1:
        #         if(intr[i][1]>=intr[i+1][0] and intr[i][1]>=intr[i+1][1]):
        #             intr.append([intr[i][0],intr[i][1]])
        #             intr.remove(intr[i])
        #             intr.remove(intr[i])
        #             intr.sort()

        #         elif(intr[i][1]>=intr[i+1][0] and intr[i][1]<intr[i+1][1]):
        #             intr.append([intr[i][0],intr[i+1][1]])
        #             intr.remove(intr[i])
        #             intr.remove(intr[i])
        #             intr.sort()
        #         else:
        #             i+=1
        #     return intr
        # b=[]
        # c=0
        # for i in range(len(intervals)-1):
        #     if(intervals[i][1]>=intervals[i+1][0]):
        #         intervals[i][1]=intervals[i+1][1]
        #         b.append(intervals[i+1])
        #         # b.pop(i+1
        #         # intervals.pop(i+1)
        # # for i in intervals:
        # #     if i in b: 
        # #         intervals.pop()

        # # return(c)
        # return(intervals)
