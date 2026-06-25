def addSum(arr,k):
    window_sum=0
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum
    
    for i in range(k,len(arr)):
        window_sum += -arr[i-k]+arr[i]
        max_sum = max(window_sum,max_sum)
    return max_sum
        
print(addSum([1,2,3,4,5],3))

