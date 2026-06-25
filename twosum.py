def two_sum(arr,target):
    seen = set()
    
    for num in arr:
        needed = target - num
        
        if needed in seen:
            return True
        
        seen.add(num)
        
    return False

print(two_sum([2,7,11,15],9))