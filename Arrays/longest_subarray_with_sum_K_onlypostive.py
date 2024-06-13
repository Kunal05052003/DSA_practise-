i=0
arr=[1,2,2,3,4,1,5]
k=4
n=len(arr)
j=0
m=0
s=arr[0]
while j<n:
    while(i<=j and s>k):
        s-=arr[i]
        i+=1
    if s==k:
        m=max(m,j-i+1)
    
    j+=1
    if j<n:
        s+=arr[j]
print(m)