def is_Sorted(arr):
    n =len(arr)
    if(n < 2):
        return True
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            return False
    return True

print(is_Sorted(arr = [1, 3, 2, 4, 5]))