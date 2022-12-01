
n = int(input())
maxNum=0
secMax=0
arr = list(map(int,input().split())) #за бързо създаване на входящи данни в масив
arr.sort()
i = len(arr)-1
j = len(arr)-1
while maxNum < arr[i]:
    maxNum+=1

if maxNum > n or maxNum == n:
    for i in arr:
        secMax = arr[j-1]
    if secMax == maxNum:
        while secMax == maxNum:
            j-=1
            secMax=arr[j]
        print(secMax)
    else:
        print(secMax)

elif maxNum < n:
    maxNum = max(arr)
    secMax = maxNum
    while secMax == maxNum:
        j-=1
        secMax = arr[j]
    print(secMax)

# Input:
# 5
# 1 2 2 3 4 4 6 6 7

# Output: (second biggest num)
# 6




    



        