def secondLargest(arr):
    max_val = float('-inf')
    sec_max = float('-inf')
    for num in arr:
        if num>max_val:
            sec_max = max_val
            max_val = num
        elif num>sec_max and num != max_val:
            sec_max = num
    return sec_max
arr = [10,24,45,21,44]
print(secondLargest(arr))