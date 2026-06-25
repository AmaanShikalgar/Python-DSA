def removeDup(arr):
    if not arr:
        return 0
    
    slow = 0
    
    for fast in range(1,len(arr)):
        if arr[fast] != arr[slow]:
            slow +=1
            arr[slow]=arr[fast]
            
    return arr[:slow+1]

print(removeDup([1,1,2,2,3]))