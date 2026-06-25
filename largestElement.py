def findLargest(arr):
    
    max_val = float('-inf')
    
    for num in arr:
        if num>max_val:
            max_val = num
            
    return max_val

arr = [10,24,45,21,44]

print(findLargest(arr))