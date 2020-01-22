import itertools
import copy
import math
from collections import defaultdict

def consecSum(arr,dp, start,end):
    if start>=end: return 0
    if start in dp: return [dp,dp[start]]
    dp[start]=max(consecSum(arr,dp,start-1,end)[1],
                  arr[start]+consecSum(arr,dp,start-2,end)[1])
    return [dp,dp[start]]
def consecIter(arr,M={}):
    M[-1]=0
    M[0]=arr[0]
    for i in range(1,len(arr)+1):
        print(i)
        M[i]=max(M[i-1],M[i-2]+arr[i-1])
    return M
def consecIter2(arr):
    a=arr[0]
    b=arr[1]
    for i in range(2,len(arr)):
        c=b
        b=a+arr[i]
        a=max(a,c)
    return max(a,b)

def miniMaxSum(arr):
    minA=[]
    maxA=[]
    tempArr=arr[:]
    while len(minA)!=4: minA.append(arr.remove(min(arr)))
    print(tempArr)
    while len(maxA)!=4: maxA.append(tempArr.remove(max(tempArr)))
    return [sum(minA), sum(maxA)]
arr=[-2,1,3,-4,5]
#print(consecSum(arr,{0:arr[0],-1:0},0,len(arr)))
#print(consecIter2(arr))
#print(consecIter2([3,7,4,6,5]))
#print(consecIter2([2,1,5,8,4]))
#print(consecIter2([3,5,-7,8,10]))
print(miniMaxSum(arr))
