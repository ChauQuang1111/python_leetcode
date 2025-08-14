def findMaxGCD(arr):
    maxValue=0
    for x in arr:
        if x >maxValue:
            maxValue=x
    count=[0]*(maxValue+1)
    for p in arr:
        count[p]=1
    for g in range(maxValue,0,-1):
        demboi=0
        for j in range (g,maxValue+1,g):
            if count[j]==1:
                demboi+=1
            if demboi>=2:return g
    return 1