def moveZero(arr):
    slow=0
    for fast in range(0,len(arr)):
        if arr[fast] != 0:
            arr[slow],arr[fast] = arr[fast],arr[slow]
            slow+=1
    return arr
print(moveZero([1,0,2]))