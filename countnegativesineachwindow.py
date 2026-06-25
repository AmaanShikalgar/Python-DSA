def count_negatives(arr,k):
    result = []
    count = 0
    n = len(arr)
    for i in range (k):
        if(arr[i]<0):
            count+=1
    result.append(count) 
    
    for i in range(k,n):
        if(arr[i-k]<0):
            count-=1
        if(arr[i]<0):
            count+=1
        result.append(count)
    return result

print(count_negatives(arr = [12, -1, -7, 8, -15, 30, 16, 28]
,k = 3))